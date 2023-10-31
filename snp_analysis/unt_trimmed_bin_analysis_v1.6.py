import os
import subprocess
import sys
import pyfiglet
from termcolor import colored

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(colored("An error occurred: ", "magenta") + str(e), file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print(colored("Analysis interrupted by user. Exiting.", "magenta"))
        sys.exit(1)

def print_chromosome_paths(chromosomes_list, bwa_base_path, bowtie_base_path):
    for chromosome in chromosomes_list:
        if chromosome == 'hg38':
            print(colored(f"\nPaths for chromosome {chromosome}:", "magenta"))
            bwa_chrom_path = f"{bwa_base_path}hg38/GRCh38_reference.fa"
            bowtie_index_path = f"{bowtie_base_path}hg38/bowtie"
            print("BWA Chromosome Path: " + bwa_chrom_path)
            print("Bowtie Index Path: " + bowtie_index_path)
        elif chromosome != 'hg38':
            print(colored(f"\nPaths for chromosome {chromosome}:", "magenta"))
            bwa_chrom_path = f"{bwa_base_path}{chromosome}_bwa_ind/Homo_sapiens.GRCh38.dna.chromosome.{chromosome}.fa"
            bowtie_index_path = f"{bowtie_base_path}{chromosome}_bowtie_ind/bowtie"
            print("BWA Chromosome Path: " + bwa_chrom_path)
            print("Bowtie Index Path: " + bowtie_index_path)

def read_accession_numbers(file_path):
    try:
        with open(file_path, 'r') as f:
            accession_numbers = [line.strip() for line in f if line.strip()]
        return accession_numbers
    except FileNotFoundError:
        print(colored("The specified file was not found. Please check the file path and try again.", "magenta"))
        sys.exit(1)
    except Exception as e:
        print(colored(f"An error occurred while reading the file: {e}", "magenta"))
        sys.exit(1)

def is_file_empty(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) == 0

def delete_intermediate_files(accession_number, chromosome):
    intermediate_files = [
        f"{accession_number}/{accession_number}.fastq",
        f"{accession_number}/{accession_number}_mapped_{chromosome}.sam",
        f"{accession_number}/{accession_number}_mapped_{chromosome}.bam",
        f"{accession_number}/{accession_number}_mapped_{chromosome}.raw.bcf",
        f"{accession_number}/{accession_number}_fastqc.zip",
        f"{accession_number}/{accession_number}_trimmed_fastqc.zip"
    ]
    for file_path in intermediate_files:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(colored(f"Deleted {file_path}", "magenta"))

def get_verified_path(prompt_message):
    while True:
        path = input(colored(prompt_message, "magenta")).strip()
        if os.path.exists(path):
            return path
        else:
            print(colored("The provided path does not exist. Please try again.", "magenta"))

def main():
    text = "CANCER IMMUNOLOGY"
    font = "banner3-D"
    terminal_width = os.get_terminal_size().columns
    f = pyfiglet.Figlet(font=font, width=terminal_width)
    logo = f.renderText(text)
    print(logo.center(terminal_width))

    bwa_base_path = "/usr/local/bin/bwa/"
    bowtie_base_path = "/usr/local/bin/bowtie/"
    trimmomatic_path = "/usr/local/bin/Trimmomatic-0.39/trimmomatic-0.39.jar"
    truseq3_path = "/usr/local/bin/Trimmomatic-0.39/adapters/TruSeq3-SE.fa"

    if not os.path.exists(bwa_base_path):
        bwa_base_path = get_verified_path("1. BWA base path not found. Please enter the correct BWA base path: ")
    if not os.path.exists(bowtie_base_path):
        bowtie_base_path = get_verified_path("2. Bowtie base path not found. Please enter the correct Bowtie base path: ")
    if not os.path.exists(trimmomatic_path):
        trimmomatic_path = get_verified_path("3. Trimmomatic path not found. Please enter the correct Trimmomatic path: ")
    if not os.path.exists(truseq3_path):
        truseq3_path = get_verified_path("4. TruSeq3 path not found. Please enter the correct TruSeq3 path: ")

    user_email = input(colored("1. Please enter your email address to receive a notification once the analysis is complete: ", "magenta")).strip()
    job_title = input(colored("2. Please enter a job title for this analysis: ", "magenta")).strip()
    accession_list_file = get_verified_path("3. Please enter the path to the accession list file: ")

    accession_numbers = read_accession_numbers(accession_list_file)
    
    all_chromosomes = [str(i) for i in range(1, 23)] + ['X', 'Y', 'hg38']
    completed_vcf_count = 0

    for accession_number in accession_numbers:
        for chromosome in all_chromosomes:
            final_vcf_file = f"{accession_number}/{accession_number}_mapped_{chromosome}.var.-final.vcf"
            if os.path.isfile(final_vcf_file) and not is_file_empty(final_vcf_file):
                completed_vcf_count += 1
                break

    print(colored(f"\nTotal accession numbers found: {len(accession_numbers)}", "magenta"))
    print(colored(f"Completed analyses with final VCF files: {completed_vcf_count}", "magenta"))
    remaining_analyses = len(accession_numbers) - completed_vcf_count
    print(colored(f"Remaining analyses to be performed: {remaining_analyses}", "magenta"))

    num_to_analyze = int(input(colored(f"4. How many of the remaining {remaining_analyses} accession numbers do you want to analyze? ", "magenta")))
    accession_numbers_to_analyze = accession_numbers[:num_to_analyze + completed_vcf_count][completed_vcf_count:]

    chromosomes_input = input(colored("5. Please enter the chromosomes to be analyzed, separated by a comma, or type 'all' to analyze all chromosomes: ", "magenta"))
    chromosomes_list = [chromosome.strip() for chromosome in chromosomes_input.split(',')] if chromosomes_input.lower() != 'all' else ['hg38']
    print_chromosome_paths(chromosomes_list, bwa_base_path, bowtie_base_path)

    remaining_accessions = len(accession_numbers_to_analyze)
    for accession_number in accession_numbers_to_analyze:
        trimmed_file = f"{accession_number}/{accession_number}_trimmed.fq.gz"
        if not os.path.isfile(trimmed_file):
            print(colored(f"\n{6}. Downloading number sequence {accession_number} from SRA... (Remaining: {remaining_accessions})", "magenta"))
            run_command(f"fastq-dump {accession_number}")

    chromosomes_input = input(colored("5. Please enter the chromosomes to be analyzed, separated by a comma, or type 'all' to analyze all chromosomes: ", "magenta"))
    chromosomes_list = [chromosome.strip() for chromosome in chromosomes_input.split(',')] if chromosomes_input.lower() != 'all' else ['hg38']
        
    if chromosomes_input.lower() != 'all':
        print_chromosome_paths(chromosomes_list, bwa_base_path, bowtie_base_path)

    for accession_number in accession_numbers_to_analyze:
        trimmed_file = f"{accession_number}/{accession_number}_trimmed.fq.gz"
        if not os.path.isfile(trimmed_file):
            # Downloading and processing steps here
            print(colored(f"\n{6}. Downloading number sequence {accession_number} from SRA... (Remaining: {remaining_accessions})", "magenta"))
            run_command(f"fastq-dump {accession_number}")
            # Add commands for processing here

        for chromosome in chromosomes_list:
            final_vcf_file = f"{accession_number}/{accession_number}_mapped_{chromosome}.var.-final.vcf"
            if os.path.isfile(final_vcf_file) and not is_file_empty(final_vcf_file):
                print(colored(f"\nVCF file for {accession_number}, chromosome {chromosome} already exists. Skipping analysis...", "magenta"))
                continue
            elif is_file_empty(final_vcf_file):
                print(colored(f"\nVCF file for {accession_number}, chromosome {chromosome} is empty. Deleting and adding to analysis...", "magenta"))
                os.remove(final_vcf_file)
        
            bwa_chrom_path = f"{bwa_base_path}{chromosome}_bwa_ind/Homo_sapiens.GRCh38.dna.chromosome.{chromosome}.fa"
            bowtie_index_path = f"{bowtie_base_path}{chromosome}_bowtie_ind/bowtie"
            
            print(colored(f"\nMapping {accession_number} reads using Bowtie2 for chromosome {chromosome}... (Remaining: {remaining_accessions})", "magenta"))
            run_command(f"bowtie2 --very-fast-local -x {bowtie_index_path} {trimmed_file} -S {accession_number}/{accession_number}_mapped_{chromosome}.sam")
         

            run_command(f"samtools view -S -b {accession_number}/{accession_number}_mapped_{chromosome}.sam > {accession_number}/{accession_number}_mapped_{chromosome}.bam")

            print(colored("\n\033[1;35m{11}. Sorting using Samtools...\033[0m ", "magenta"))
            run_command(f"samtools sort {accession_number}/{accession_number}_mapped_{chromosome}.bam > {accession_number}/{accession_number}_mapped_{chromosome}.sorted.bam")

            print(colored("\n\033[1;35m{12}. Summarizing the base calls (mpileup)...\033[0m ", "magenta"))
            run_command(f"bcftools mpileup -f {bwa_chrom_path} {accession_number}/{accession_number}_mapped_{chromosome}.sorted.bam | bcftools call -mv -Ob -o {accession_number}/{accession_number}_mapped_{chromosome}.raw.bcf")

            print(colored("\n\033[1;35m{13}. Finalizing VCF...\033[0m ", "magenta"))
            run_command(f"bcftools view {accession_number}/{accession_number}_mapped_{chromosome}.raw.bcf | vcfutils.pl varFilter - > {final_vcf_file}")

            # Delete intermediate files to save disk space
            delete_intermediate_files(accession_number, chromosome)
        remaining_accessions -= 1
    send_email_command = f'sendemail -f sudoroot1775@outlook.com -t {user_email} -u "{job_title}_Analysis Done" -m "Ready to receive information for the next analysis." -s smtp-mail.outlook.com:587 -o tls=yes -xu sudoroot1775@outlook.com -xp ydAEwVVu2s7uENC'
    os.system(send_email_command)

if __name__ == "__main__":
    main()
