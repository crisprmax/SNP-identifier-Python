#!/usr/bin/env python3

import os
import shutil
import subprocess
from pathlib import Path
import signal
import importlib

packages = ['os', 'shutil', 'subprocess', 'pathlib', 'signal']

# Check if packages are installed, install them if necessary
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        print(f'{package} is not installed. Installing...')
        subprocess.run(['pip', 'install', package])

# Define color codes
RED = '\033[1;31m'
GREEN = '\033[1;32m'
MAGENTA = '\033[1;35m'
BLUE = '\033[1;34m'
RESET = '\033[0m'

def replace_file_on_interrupt(sig, frame):
    # Remove the untrimmed_bash_sra_v1.2.txt file
    os.remove('untrimmed_bash_sra_v1.2.txt')
    print('\nRemoving untrimmed_bash_sra_v1.2.txt...')
    exit(1)

# Register the signal handler
signal.signal(signal.SIGINT, replace_file_on_interrupt)

# THIS PROGRAM IS FOR UNTRIMMED WHOLE ANALYSIS

bash_script = f"""#!/bin/bash

# Define the path of the potential trimmed file
TRIMMED_FILE="SRR_one/SRR_one_trimmed.fq.gz"

# Check if the trimmed file already exists
if [ ! -f "$TRIMMED_FILE" ]; then
    echo -e "\n\033[1;35mDownloading number sequence SRR_one from SRA...\033[0m "
    fastq-dump SRR_one

    if [ -d "SRR_one" ]; then
      rm -r "SRR_one"
    fi

    mkdir SRR_one
    mv SRR_one.fastq SRR_one

    echo -e "\n\033[1;35mRunning fastqc on SRR_one...\033[0m "
    fastqc SRR_one/SRR_one.fastq

    echo -e "\n\033[1;35mTrimming SRR_one...\033[0m "
    java -jar trim_path SE SRR_one/SRR_one.fastq SRR_one/SRR_one_trimmed.fq.gz ILLUMINACLIP:truseq3_path:2:30:10 SLIDINGWINDOW:4:20 MINLEN:35

    echo -e "\n\033[1;35mRunning fastqc on trimmed SRR_one...\033[0m "
    fastqc SRR_one/SRR_one_trimmed.fq.gz
else
    echo -e "\n\033[1;32mTrimmed file already exists. Skipping download, trimming, and quality check...\033[0m"
fi

echo -e "\n\033[1;35mMapping SRR_one reads using Bowtie2...\033[0m "
bowtie2 --very-fast-local -x bowtie_index_path SRR_one/SRR_one_trimmed.fq.gz -S SRR_one/SRR_one_mapped.sam

samtools view -S -b SRR_one/SRR_one_mapped.sam > SRR_one/SRR_one_mapped.bam

echo -e "\n\033[1;35mSorting using Samtools...\033[0m "
samtools sort SRR_one/SRR_one_mapped.bam > SRR_one/SRR_one_mapped.sorted.bam

echo -e "\n\033[1;35mSummarizing the base calls (mpileup)...\033[0m "
bcftools mpileup -f bwa_chrom_path SRR_one/SRR_one_mapped.sorted.bam | bcftools call -mv -Ob -o SRR_one/SRR_one_mapped.raw.bcf

echo -e "\n\033[1;35mFinalizing VCF...\033[0m "
bcftools view SRR_one/SRR_one_mapped.raw.bcf | vcfutils.pl varFilter - > SRR_one/SRR_one_mapped.var.-final.vcf

rm SRR_one/SRR_one.fastq SRR_one/SRR_one_mapped.sam SRR_one/SRR_one_mapped.bam SRR_one/SRR_one_mapped.sorted.bam SRR_one/SRR_one_mapped.raw.bcf SRR_one/SRR_one_fastqc.zip SRR_one/SRR_one_trimmed_fastqc.zip

"""

with open("untrimmed_bash_sra_v1.2.txt", "w") as f:
    f.write(bash_script)

# THIS PROGRAM IS FOR UNTRIMMED WHOLE ANALYSIS

# Define functions to replace text in files
def replace_text(file_path, old_text, new_text):
    with open(file_path, 'r+') as file:
        text = file.read().replace(old_text, new_text)
        file.seek(0)
        file.write(text)
        file.truncate()

def replace_in_untrimmed_bash_srr(old_text, new_text):
    replace_text('untrimmed_bash_sra_v1.2.txt', old_text, new_text)


# Get the current working directory
cwd = Path.cwd()
print('\n')


# Add the email to be notified when the process is done
user = input(f'{MAGENTA}1){RESET} Enter the email address to be notified once the analysis is complete: ')

# Add the job title
job_title = input(f'{MAGENTA}2){RESET} Enter a job name: ')


jar_file = '/usr/local/bin/Trimmomatic-0.39/trimmomatic-0.39.jar'
jar_path = os.path.expanduser(jar_file)


if os.path.exists(jar_path):
    trim_path = jar_path
    replace_in_untrimmed_bash_srr('trim_path', trim_path)
    print(f'{MAGENTA}3){RESET} {jar_path} is the absolute path.')
else:
    print(f'NOTE: {jar_path} does not match your absolute path.')
    print('You have a different path for trimmomatic-0.39.jar')
    trim_path = input(f'{MAGENTA}3){RESET} Copy and paste the absolute path to your trimmomatic-0.39.jar file: ')
    replace_in_untrimmed_bash_srr('trim_path', trim_path)



seq3_file = '/usr/local/bin/Trimmomatic-0.39/adapters/TruSeq3-SE.fa'
seq3_path = os.path.expanduser(seq3_file)

if os.path.exists(seq3_path):
    truseq3_path = seq3_path
    replace_in_untrimmed_bash_srr('truseq3_path', truseq3_path)
    print(f'{MAGENTA}4){RESET} {seq3_path} is the absolute path.')
else:
    print(f'NOTE: {seq3_path} does not match your absolute path.')
    print('You have a different path for TruSeq3-SE.fa')
    truseq3_path = input(f'{MAGENTA}4){RESET} Copy and paste the absolute path to your TruSeq3-SE.fa file: ')
    replace_in_untrimmed_bash_srr('truseq3_path', truseq3_path)

# Ask the user if they want to analyze the whole genome or specific chromosomes
analysis_scope = ""
while analysis_scope not in ["1", "2"]:
    analysis_scope = input(f"{MAGENTA}Would you like to analyze the whole genome or specific chromosomes?\n1) Whole Genome\n2) Specific Chromosomes\nEnter the number corresponding to your choice: {RESET}")
    if analysis_scope not in ["1", "2"]:
        print(f"{RED}Invalid choice. Please enter 1 for Whole Genome or 2 for Specific Chromosomes.{RESET}")

# If Whole Genome
if analysis_scope == "1":
    bwa_chrom_path = "/usr/local/bin/bwa/hg38/GRCh38_reference.fa"
    bowtie_index_path = "/usr/local/bin/bowtie/hg38/bowtie"
    chroms_to_analyze = ['whole_genome']
else:  # Specific Chromosomes
    valid_chromosomes = list(map(str, range(1, 23))) + ["X", "Y"]
    chroms_to_analyze = []
    print(f"{MAGENTA}Enter the chromosome numbers separated by comma (e.g., 1,2,X,Y) to be analyzed:{RESET}")
    input_chroms = input().split(',')
    for chrom in input_chroms:
        if chrom.strip() in valid_chromosomes:
            chroms_to_analyze.append(chrom.strip())
        else:
            print(f"{RED}Invalid chromosome: {chrom}. Skipping.{RESET}")

# These commands will replace each SRA number on .txt file with each of the accession numbers entered by user
for index, sra in enumerate(sra_list):
    for chromosome in chroms_to_analyze:
        if chromosome != 'whole_genome':
            # Construct the paths for BWA and Bowtie files based on the chromosome
            bwa_chrom_path = f"/usr/local/bin/bwa/{chromosome}_bwa_ind/Homo_sapiens.GRCh38.dna.chromosome.{chromosome}.fa"
            bowtie_index_path = f"/usr/local/bin/bowtie/{chromosome}_bowtie_ind/bowtie"
        print(f"{MAGENTA}Analyzing Chromosome: {chromosome} for SRA: {sra}{RESET}")
        print(f"{MAGENTA}Bowtie Index Path: {RESET}{bowtie_index_path}")
        print(f"{MAGENTA}BWA Chromosome Path: {RESET}{bwa_chrom_path}")
        
        # Update paths and placeholders
        replace_in_untrimmed_bash_srr('number', placement[index])
        replace_in_untrimmed_bash_srr('SRR_one', sra)
        replace_in_untrimmed_bash_srr('bowtie_index_path', bowtie_index_path)
        replace_in_untrimmed_bash_srr('bwa_chrom_path', bwa_chrom_path)
        
        # Run the commands on the untrimmed_bash_sra_v1.2.txt file
        subprocess.run(['bash', str(cwd) + '/untrimmed_bash_sra_v1.2.txt'])
        
        # Replace the changed names back to original
        replace_in_untrimmed_bash_srr(placement[index], 'number')
        replace_in_untrimmed_bash_srr(sra, 'SRR_one')

# Reset the paths
replace_in_untrimmed_bash_srr(trim_path, 'trim_path')
replace_in_untrimmed_bash_srr(truseq3_path, 'truseq3_path')
replace_in_untrimmed_bash_srr(bowtie_index_path, 'bowtie_index_path')
replace_in_untrimmed_bash_srr(bwa_chrom_path, 'bwa_chrom_path')


#run the commands on the sendemail.txt file
print('Sending email to ' + user + ' ....')
os.system('sendemail -f sudoroot1775@outlook.com -t ' + user + ' -u ' + job_title + '_Analysis Done -m "Ready to receive information for the next analysis." -s smtp-mail.outlook.com:587 -o tls=yes -xu sudoroot1775@outlook.com -xp ydAEwVVu2s7uENC')


def run_analysis():
    #Runs untrimmed_analysis_tools.py and prompts user to continue or exit.
    print(f'{MAGENTA}untrimmed_analysis_tools is ready to run.{RESET} \n')
    while True:
        print(f'{MAGENTA}Would you like to run another analysis? {RESET}')
        choice = input('Enter yes/no to continue: ')
        if choice.lower() == 'yes':
            print(f'{MAGENTA} 1) {RESET} Email address used: ', user)
            print(f'{MAGENTA} 2) {RESET} trimmomatic-0.39.jar file path: ', trim_path)
            print(f'{MAGENTA} 3) {RESET} TruSeq3 file path: ', truseq3_path)
            print(f'{MAGENTA} 4) {RESET} Bowtie file path: ', bowtie_index_path)
            print(f'{MAGENTA} 5) {RESET} BWA reference chromosome path: ', bwa_chrom_path)
            print(f'{MAGENTA} 6) {RESET} Accession list file name: ', accession)
            os.system('python3 /usr/local/bin/untrimmed_bin_analysis.py')

        elif choice.lower() == 'no':
            print(f'{MAGENTA} Analysis terminated. Goodbye. {RESET}')
            break
        else:
            print(f'{MAGENTA} Enter either yes or no.{RESET} ')

os.remove('untrimmed_bash_sra_v1.2.txt')

run_analysis()


