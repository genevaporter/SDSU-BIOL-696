#!/bin/bash -i

### starting fresh, I created the directory biol696-1 so it would be easier to manage.

rm -r ~/biol696-1
mkdir ~/biol696-1
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/Porter_backup.sh ~/biol696-1/

### Make this a bash script that can be executed by putting
### a "shebang" at the top of the file (done, line 1)

echo "It works!"

### Execute command that prints every command as it is executed

set -o xtrace

### Make an alias called 'll' that is equal to 'ls -al'
### The alias is not being recognized in my scrpit, so I made a function instead.

ll() {
      ls -al
     }
export -f ll

### (1) In your home directory make a directory called RAW_DATA

mkdir ~/biol696-1/RAW_DATA
cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/Porter_fasta_script.sh ~/biol696-1/RAW_DATA/

### (2) Copy all .fna fasta files  
###     from home directory into RAW_DATA (must work from any directory.)

cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/*.fna ~/biol696-1/RAW_DATA

### (3) Do the same with all primer files ending with .csv

cp ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/*.csv ~/biol696-1/RAW_DATA

### (4) In your home directory, make 2 directories: P_DATA and RESULTS

mkdir ~/biol696-1/P_DATA ~/biol696-1/RESULTS

### (5) Add all three directories to your $PATH: ~/RAW_DATA, ~/P_DATA
###     and ~/RESULTS

export PATH=$PATH:~/biol696-1/RAW_DATA:~/biol696-1/P_DATA:~/biol696-1/RESULTS

### (6) Write your entire $PATH, the name RAW_DATA and the 
###    contents of this directory into a new file 
###    called 'readme.txt' in your home directory

> ~/biol696-1/readme.txt
echo $PATH >> ~/biol696-1/readme.txt
printf "\n" >> ~/biol696-1/readme.txt
echo 'RAW_DATA' >> ~/biol696-1/readme.txt
cd ~/biol696-1/RAW_DATA
ll >> ~/biol696-1/readme.txt

### (7) The last command should dump the contents of readme.txt
###     to the terminal.

cat ~/biol696-1/readme.txt
