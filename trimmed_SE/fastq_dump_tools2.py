#!/usr/bin/env python3
import os
import shutil

#THIS PROGRAM IS FOR TRIMMED FILES ONLY

#you need to install pytul using your terminal "pip3 install python-util"
from pyutil import filereplace

#must have sendemail installed on terminal
#for ubuntu use: $ sudo apt-get install libio-socket-ssl-perl libnet-ssleay-perl sendemail
# for Mac, use: brew install sendemail

# getting the current working directory
src_dir = os.getcwd()# printing current directory
print('\033[1;45m This is your current working directory:' + src_dir + '\033[0;0;0m')
print('\033[1;45m In Linux, use the command "readlink -f file.txt" in order to get the complete path.\033[0;0;0m')
print('\033[1;45m In MacOS, use the command "realpath file.txt" in order to get the complete path.\033[0;0;0m')

#add the email to be notified when the process is done
user = input('Enter the email address to be notified once the analysis is complete: ')
filereplace('commands_srr2.txt', 'user_email', user)

#add the job title
job = input('Enter a job name: ')
filereplace('commands_srr2.txt', 'job_name', job)

#add the path to where bowtie files are found (must end in "bowtie/bowtie")
bowtie = input('Copy and paste the complete path to your bowtie files: ')
filereplace('commands_srr2.txt', 'bowtie2_path', bowtie)

#add the path to where reference chromosome is found
ref_chrom = input('Copy and paste the complete path to your reference chromosome: ')
filereplace('commands_srr2.txt', 'ref_chrom', ref_chrom)

#this asks user to type in 10 accession numbers
srr_one = input('Please paste the 1st SRA accession number: ')
srr_two = input('Please paste the 2nd SRA accession number: ')
srr_thr = input('Please paste the 3rd SRA accession number: ')
srr_fou = input('Please paste the 4th SRA accession number: ')
srr_fiv = input('Please paste the 5th SRA accession number: ')
srr_six = input('Please paste the 6th SRA accession number: ')
srr_sev = input('Please paste the 7th SRA accession number: ')
srr_eig = input('Please paste the 8th SRA accession number: ')
srr_nin = input('Please paste the 9th SRA accession number: ')
srr_ten = input('Please paste the 10th SRA accession number: ')



#these commands will replace each SRR number on .txt file with 
#each of the ten accession numbers entered by user
filereplace('commands_srr2.txt',"SRR_one", srr_one)
filereplace('commands_srr2.txt',"SRR_two", srr_two)
filereplace('commands_srr2.txt',"SRR_thr", srr_thr)
filereplace('commands_srr2.txt',"SRR_fou", srr_fou)
filereplace('commands_srr2.txt',"SRR_fiv", srr_fiv)
filereplace('commands_srr2.txt',"SRR_six", srr_six)
filereplace('commands_srr2.txt',"SRR_sev", srr_sev)
filereplace('commands_srr2.txt',"SRR_eig", srr_eig)
filereplace('commands_srr2.txt',"SRR_nin", srr_nin)
filereplace('commands_srr2.txt',"SRR_ten", srr_ten)

#this will run the commands on the commands_srr2.txt file
os.system('cat commands_srr2.txt | bash')

print('\033[1;45m The previous input sequences have been analyzed.\033[0;0;0m')

# copying the files
shutil.copyfile('commands_srr_template_gen2.txt', 'commands_srr2.txt') #copy src to destin

#printing the sorted list of unanalyzed files
print('\033[1;45m These are the unanalyzed files in the present directory:\033[0;0;0m ') 
files = os.listdir()
files.sort()
files = files[files.index(srr_ten)+1 : ]
print(files)

print('\033[1;45m fastq_dump_tools is ready to run.\033[0;0;0m')

print('\033[1;45m Would you like to run another analysis? \033[0;0;0m')

while True:
    a = input('Enter yes/no to continue: ')
    if a=="yes":
        print('\033[1;45m This was the email address used:\033[0;0;0m ', user)
        print('\033[1;45m This was your TruSeq3 file path:\033[0;0;0m ', tru_seq)
        print('\033[1;45m This was your Bowtie files path:\033[0;0;0m ', bowtie)
        print('\033[1;45m This was your reference chromosome path:\033[0;0;0m ', ref_chrom)
        os.system('python3 fastq_dump_tools2.py')
        continue
    elif a=="no":
        print('\033[1;45m Analysis terminated.\033[0;0;0m')
        break
    else:
        print('\033[1;45m Enter either yes/no:\033[0;0;0m ')


