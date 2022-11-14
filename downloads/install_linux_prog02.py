#!/usr/bin/env python3
<<<<<<< Updated upstream

import os
import sys
 
import subprocess

print("\033[1;45m ONLY RUN THIS PROGRAM IN YOUR HOME DIRECTORY  \033[0;0;0m")
print("\033[1;45m to access your home directory use the command: '$ explorer.exe .' only on Ubuntu WSL  \033[0;0;0m")
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')

print("\033[1;45m Installing Python3 and pip3 \033[0;0;0m")
subprocess.call(['sudo', 'apt', 'install', 'python3', 'python3-pip'])

import pip
=======
import os
import sys
import pip 
import subprocess

print("\033[1;45m ONLY RUN THIS PROGRAM IN YOUR HOME DIRECTORY  \033[0;0;0m")
print('\n')
print("\033[1;45m To access your homedirectory use the command: $ 'explorer.exe .' on Ubuntu WSL only!  \033[0;0;0m")
input("Press Enter to continue...")
>>>>>>> Stashed changes

#Update terminal and install necessaries 
print("\033[1;45m Updating terminal  \033[0;0;0m")
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('sudo apt-get update -y')
os.system('sudo apt-get upgrade -y')
print('\n')
<<<<<<< Updated upstream

#checking for the installation of wget
print('\033[1;45m Checking for the installation of wget \033[0;0;0m')
=======
#checking for the installation of wget
print('\033[1;45m Checking for the installation of wget \033[0;0;0m')

>>>>>>> Stashed changes
if os.system('wget --version') == 0:
    print('\033[1;45m wget is installed \033[0;0;0m')
else:
    print('\033[1;45m wget is not installed \033[0;0;0m')
<<<<<<< Updated upstream
    print('\033[1;45m installing wget \033[0;0;0m')
    os.system('sudo apt-get install wget -y')
    print('\033[1;45m wget is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#checking for the installation of unzip
print('\033[1;45m Checking for the installation of unzip \033[0;0;0m')
if os.system('unzip --version') == 0:
    print('\033[1;45m unzip is installed \033[0;0;0m')
else:
    print('\033[1;45m unzip is not installed \033[0;0;0m')
    print('\033[1;45m installing unzip \033[0;0;0m')
    os.system('sudo apt-get install unzip -y')
    print('\033[1;45m unzip is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#checking for the installation of sendemail
print('\033[1;45m Checking for the installation of sendemail \033[0;0;0m')
if os.system('sendemail --version') == 0:
    print('\033[1;45m sendemail is installed \033[0;0;0m')
else:
    print('\033[1;45m sendemail is not installed \033[0;0;0m')
    print('\033[1;45m installing sendemail \033[0;0;0m')
    os.system('sudo apt-get install sendemail -y')
    print('\033[1;45m sendemail is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#checking for the installation of xdg-utils
print('\033[1;45m Checking for the installation of xdg-utils \033[0;0;0m')
if os.system('xdg-open --version') == 0:
    print('\033[1;45m xdg-utils is installed \033[0;0;0m')
else:
    print('\033[1;45m xdg-utils is not installed \033[0;0;0m')
    print('\033[1;45m installing xdg-utils \033[0;0;0m')
    os.system('sudo apt-get install xdg-utils -y')
    print('\033[1;45m xdg-utils is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#checking for the installation of tabix
print('\033[1;45m Checking for the installation of tabix \033[0;0;0m')
if os.system('tabix --version') == 0:
    print('\033[1;45m tabix is installed \033[0;0;0m')
else:
    print('\033[1;45m tabix is not installed \033[0;0;0m')
    print('\033[1;45m installing tabix \033[0;0;0m')
    os.system('sudo apt-get install tabix -y')
    print('\033[1;45m tabix is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#downloading SRA Toolkit, you can also try sudo apt install sra-toolkit (do not need to enter export path)
print('\033[1;45m Downloading SRA Toolkit \033[0;0;0m')
os.system('wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz')
os.system('tar -xvzf sratoolkit.current-ubuntu64.tar.gz')
os.system('rm sratoolkit.current-ubuntu64.tar.gz')
os.system('mv sratoolkit.2.10.9-ubuntu64 sratoolkit')
os.system('export PATH=$PATH:~/sratoolkit/bin')
os.system('sudo apt install sra-toolkit')
print('\033[1;45m SRA Toolkit is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')
=======
    input('\033[1;45m Press enter to install wget \033[0;0;0m \n')
    os.system('sudo apt-get install wget -y')
print('\n')
print('\033[1;45m Checking for the installation of unzip \033[0;0;0m')
os.system('sudo apt-get install unzip')
os.system('sudo apt-get install libio-socket-ssl-perl libnet-ssleay-perl sendemail')
os.system('sudo apt-get install --reinstall xdg-utils')
os.system('sudo apt-get install tabix')


#Check Python version
if sys.version_info.major == 3:
    print('\033[1;45m Python3 is installed. \033[0;0;0m')
else:
    print('\033[0;101m You need to install a current version of Python3 \033[0;0;0m')

#Check Pip version
pip_versn = pip.__version__
print('\033[1;45m Your Pip version is ' + pip_versn + '\033[0;0;0m')
print('\033[1;45m Note, if you do not have Pip installed, install it using the command: sudo apt install python3-pip \033[0;0;0m')
os.system('pip3 install python-util')

#downloading SRA Toolkit, you can also try sudo apt install sra-toolkit (do not needt to enter export path)
print('\033[1;45m Downloading SRA Toolkit \033[0;0;0m')
os.system('wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz')

#extract tar file contents
os.system('tar -vxzf sratoolkit.tar.gz')
print('\033[1;45m Extracted SRA Toolkit files \033[0;0;0m')

#remove SRA Toolkit tar file
os.system('rm sratoolkit.tar.gz')

#show files in the current directory
print('\033[1;45m These are the files in the current directory: \033[0;0;0m')
os.system('ls')

#add export path to the $path directory
sra_tool = input('\033[1;45m Copy and paste the file name of the sratoolkit: \033[0;0;0m \n')
print('\033[1;45m This is your export path: \033[0;0;0m export PATH=$PATH:$PWD/' + sra_tool + '/bin \n')
print('\033[1;45m The following 6 steps must be followed carefully: \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 1) Open another terminal window (TW)\033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 2) Copy and paste the command "vim ~/.bashrc" into the TW and press "Enter" \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 3) Enter "I" on the TW and press "Enter" \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 4) Copy and paste the following path below the last line of the TW: \033[0;0;0m export PATH=$PATH:$PWD/' + sra_tool + '/bin')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 5) Press the following keys on the TW in the correct order: "Esc", ":", "w", "q", "Enter" \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\033[1;45m 6) If Vim closed correctly, you may now close the new terminal window \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
>>>>>>> Stashed changes

#install fastqc
print('\033[1;45m Ready to install FASTQC \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('sudo apt-get install -y fastqc')
<<<<<<< Updated upstream
print('\033[1;45m FASTQC is installed \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#checking for the installation of java
print('\033[1;45m Checking for the installation of java \033[0;0;0m')
if os.system('java -version') == 0:
    print('\033[1;45m java is installed \033[0;0;0m')
else:
    print('\033[1;45m java is not installed \033[0;0;0m')
    print('\033[1;45m installing java \033[0;0;0m')
    os.system('sudo apt-get install default-jre -y')
    os.system('sudo apt-get install default-jdk -y')
    print('\033[1;45m java is installed \033[0;0;0m')

input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
=======
print('\n')

#install java
print('\033[1;45m Ready to install Java \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('sudo apt install default-jre')
print('\n')
print('\033[1;45m Ready to install Java SE Development Kit (JDK) \033[0;0;0m')
print('\033[1;45m This will open a webpage where you can download the approprite JDK \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('xdg-open https://www.oracle.com/java/technologies/downloads/')
input('\033[1;45m Press enter after JDK is installed to test Java... \033[0;0;0m \n')
print('\033[1;45m Testing Java \033[0;0;0m')
os.system('java -version')
>>>>>>> Stashed changes
print('\n')

#install trimmomatic
print('\033[1;45m Ready to install Trimmomatic \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
os.system('wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip')
os.system('unzip Trimmomatic-0.39.zip')
os.system('rm Trimmomatic-0.39.zip')
os.system('mkdir -p local/bin')
os.system('sudo cp Trimmomatic-0.39/trimmomatic-0.39.jar $HOME/local/bin')
<<<<<<< Updated upstream
os.system('sudo chmod 755 $HOME/local/bin/trimmomatic-0.39.jar')
input('\033[1;45m Press enter to test Trimmomatic... \033[0;0;0m \n')
print('\033[1;45m Checking if Trimmomatic was properly installed \033[0;0;0m')
os.system('java -jar $HOME/local/bin/trimmomatic-0.39.jar')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#install bwa
print('\033[1;45m Installing BWA \033[0;0;0m')
os.system('sudo apt-get install bwa -y')
print('\033[1;45m BWA is installed \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#install Bowtie2
print('\033[1;45m Installing Bowtie2 \033[0;0;0m')
os.system('sudo apt-get install bowtie2 -y')
print('\033[1;45m Bowtie2 is installed \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#install samtools
print('\033[1;45m Installing samtools \033[0;0;0m')
os.system('sudo apt-get install samtools -y')
print('\033[1;45m samtools is installed \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
print('\n')

#install bcftools
print('\033[1;45m Installing bcftools \033[0;0;0m')
os.system('sudo apt-get install bcftools -y')
print('\033[1;45m bcftools is installed \033[0;0;0m')
input('\033[1;45m Press enter to continue... \033[0;0;0m \n')
=======
input('\033[1;45m Press enter to test Trimmomatic... \033[0;0;0m \n')
print('\033[1;45m Checking if Trimmomatic was properly installed \033[0;0;0m')
os.system('java -jar $HOME/local/bin/trimmomatic-0.39.jar')
print('\n')

#install other programs
print('\033[1;45m Installing BWA \033[0;0;0m')
os.system('sudo apt-get install -y bwa')
print('\n')
print('\033[1;45m Installing Bowtie2 \033[0;0;0m')
os.system('sudo apt-get install -y bowtie2')
print('\n')
print('\033[1;45m Installing Samtools \033[0;0;0m')
os.system('sudo apt-get install -y samtools')
print('\n')
print('\033[1;45m Installing BCFtools \033[0;0;0m')
os.system('sudo apt-get install -y bcftools')

>>>>>>> Stashed changes
print('\n')
print('\033[1;45m All tools have been installed \033[0;0;0m')
print('\033[1;45m Finish setting up the SRA Toolkit with the command "vdb-config -i" \033[0;0;0m')

