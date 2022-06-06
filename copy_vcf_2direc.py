import os
from os import listdir
from os.path import join, isfile
import shutil
from shutil import copyfile


print('Use the command "readlink -f name_of_file/dir" in order to get the complete path.')


directory = input('\033[1;45m Enter the name of the directory you wish to create and copy all vcf files to: \033[0;0;0m ')

print('\n')
homedir = input('\033[1;45m Enter the path where the SRR directories are currently stored: \033[0;0;0m ')


isecdir = os.path.join(homedir, directory)

os.mkdir(isecdir)
print('\n')
print('\033[1;45m New directory has been created: \033[0;0;0m ' + directory)

print('\n')
print('\033[1;45m Copying all vcf files to: \033[0;0;0m ' + directory)


for item in listdir(homedir):
    if 'SRR' or 'ERR' in item:
        subdir = os.path.join(homedir, item)
        for content in listdir(subdir):
            if '.vcf' in content:
                copyfile(os.path.join(subdir, content),
                         os.path.join(isecdir, content))
            else: pass
    else: pass
print('\n')
print('\033[1;45m All vcf files have been copied to: \033[0;0;0m ' + directory)

