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
print('\033[1;45m This is your current working directory:' + src_dir + '\033[0m')
print('\033[1;45m Use the command "realpath file.txt" in order to get the complete path.\033[0m')

#add the email to be notified when the process is done
user = input('Enter the email address to be notified once the analysis is complete: ')
filereplace('sendemail.txt', 'user_email', user)

#add the job title
job = input('Enter a job name: ')
filereplace('sendemail.txt', 'job_name', job)

#add the path to where bowtie files are found (must end in "bowtie/bowtie")
bowtie = input('Copy and paste the complete path to your bowtie files: ')
filereplace('trimmed_bash_srr.txt', 'bowtie2_path', bowtie)

#add the path to where reference chromosome is found
ref_chrom = input('Copy and paste the complete path to your reference chromosome: ')
filereplace('trimmed_bash_srr.txt', 'ref_chrom', ref_chrom)

#printing the sorted list of unanalyzed files
print('\033[1;45m These are the unanalyzed files in the present directory:\033[0m ') 
files = os.listdir()
new = []
cdir = os.getcwd()
for i in files:
    if 'RR' in i and '.txt' not in i:
        new.append(i)

vcfs = []
for j in new:
    srr_dirc = os.path.join(cdir, j)
    content = os.listdir(srr_dirc)
    for doc in content:
        if '_mapped.var.-final.vcf' in doc:
            name = doc
            name = name.replace('_mapped.var.-final.vcf', '')
            vcfs.append(name)

for i in vcfs:
    if i in new:
        new.remove(i)
new.sort()
print(new)

length = len(new)
print(f'*** There are {length} unanalyzed files ***')

#this asks user to type in accession numbers
number = int(input('How many SRA sequences do you wish to analyze: '))

#this will store placement numbers into a list
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
number = number + 1
placement = [ordinal(n) for n in range(1, number)]

#this will set different variables for different srr sequences
srr_list = new[0:number-1]

#these commands will replace each SRR number on .txt file with 
#each of the accession numbers entered by user
for index in range(len(srr_list)):
    filereplace('trimmed_bash_srr.txt',"number", placement[index])
    filereplace('trimmed_bash_srr.txt',"now", srr_list[index])

    #run the commands on the trimmed_bash_srr.txt file
    os.system('cat trimmed_bash_srr.txt | bash')

    #replace the changed names back to orginal
    filereplace('trimmed_bash_srr.txt', placement[index], "number")
    filereplace('trimmed_bash_srr.txt', srr_list[index], "now")

#run the commands on the sendemail.txt file
os.system('cat sendemail.txt | bash')

#reset the sendemail command
filereplace('sendemail.txt', user, 'user_email')
filereplace('sendemail.txt', job, 'job_name')

#reset the bowtie2_path and refchrome path
filereplace('trimmed_bash_srr.txt', bowtie, 'bowtie2_path')
filereplace('trimmed_bash_srr.txt', ref_chrom, 'ref_chrom')

# copying the files
#shutil.copyfile('commands_srr_template_gen2.txt', 'trimmed_bash_srr.txt') #copy src to destin

print('\033[1;45m trimmed_analysis_tools is ready to run.\033[0;0;0m')

print('\033[1;45m Would you like to run another analysis? \033[0;0;0m')

while True:
    a = input('Enter yes/no to continue: ')
    if a=="yes":
        print('\033[1;45m This was your Bowtie files path:\033[0;0;0m ', bowtie)
        print('\033[1;45m This was your reference chromosome path:\033[0;0;0m ', ref_chrom)
        os.system('python3 trimmed_analysis_tools.py')
        continue
    elif a=="no":
        print('\033[1;45m Analysis terminated. Goodbye. \033[0;0;0m')
        break
    else:
        print('\033[1;45m Enter either yes/no:\033[0;0;0m ')
