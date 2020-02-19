#!/bin/bash

### Make this a bash script that can be executed by putting a "shebang" at the top.
echo "Started script Porter_project_bash.sh."


### Execute command that prints every command as it is executed
set -x


### Make an alias called 'll' that is equal to 'ls -al'
# The alias is not being recognized in my scrpit, so I made a function instead.
ll() 
    {
    ls -al
    }


### (1) In your home directory make a directory called RAW_DATA
mkdir -p ~/RAW_DATA


### (2) Copy all .fna fasta files  
###     from home directory into RAW_DATA (must work from any directory.)
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/*.fna ~/RAW_DATA


### (3) Do the same with all primer files ending with .csv
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/*.csv ~/RAW_DATA


### (4) In your home directory, make 2 directories: P_DATA and RESULTS
mkdir -p ~/P_DATA ~/RESULTS


### (5) Add all three directories to your $PATH: ~/RAW_DATA, ~/P_DATA
###     and ~/RESULTS
export PATH=$PATH:~/RAW_DATA:~/P_DATA:~/RESULTS


### (6) Write your entire $PATH, the name RAW_DATA and the 
###    contents of this directory into a new file 
###    called 'readme.txt' in your home directory
> ~/readme.txt
echo PATH >> ~/readme.txt
echo $PATH >> ~/readme.txt
printf "\n" >> ~/readme.txt
echo 'RAW_DATA' >> ~/readme.txt
cd ~/RAW_DATA 
ll >> ~/readme.txt


### (7) The last command should dump the contents of readme.txt
###     to the terminal.
cat ~/readme.txt


### The following commands are needed for running Porter_fasta_script.sh and Porter_backup.sh.
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/Porter_fasta_script.sh ~/RAW_DATA/
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/Porter_backup.sh ~/



