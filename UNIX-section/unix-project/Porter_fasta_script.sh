#!/bin/bash

### (1) Ask the user for a fasta file for analysis. 
### For this exercise, use the file bigdata.fna which should be in ~/RAW_DATA
read -p "Enter fasta filename: " fn


### (2) Check to see if the file exists. If not, the function exits. 
if [[ ! -f ./$fn ]]; then
   echo "The file does not exist. Exiting..."
   exit 1
fi
echo You entered $fn


### (3) Split up the bigdata.fna into separate smaller .fna files of 50,000 sequences each.
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%50000==0){file=sprintf("myseq%.6d.fna",n_seq);} print > file; n_seq++; next;} { print > file; }' < ./$fn


### (4) Use grep to check how many fasta sequences are in all of the .fna files and redirect this to a file in RAW_DATA called 'log.txt'
echo "Number of fasta sequences in each .fna file:" > ./log.txt
grep '>' -c *.fna >> ./log.txt
printf "\n" >> ./log.txt


### (5) Dump the output of log.txt to the terminal 
cat ./log.txt


### (6) The for loop below cycles though every file in the current directory and prints them.
###     The awk script below removes all the line breaks from fasta files.
###     TASK: Change the for loop so that it runs the awk command on all of the my*fna files and
###           outputs a new file with a .txt extension.
for f in myseq*.fna
do
    awk 'BEGIN{RS=">"}{gsub("\n","",$0); print ">"$0}' $f > $f'.txt'
done


### (7) Use a for loop to count all the instances of the following string in all of the .fna.txt
###     files: 'CACCCTCTCAGGTCGGCTACGCATCGTCGCC'. Have the grep results for all files appended 
###     to log.txt, then show the contents of log.txt in the terminal
echo "Instances of CACCCTCTCAGGTCGGCTACGCATCGTCGCC:" >> ./log.txt
for fn in myseq*.fna.txt
do
    (echo -n $fn':'; grep -c 'CACCCTCTCAGGTCGGCTACGCATCGTCGCC' ./$fn) >> ./log.txt
done
printf "\n" >> ./log.txt
cat ./log.txt


### (8) Move all the .fna.txt files to the directory ~/P_DATA
for file in *.fna.txt
do
    mv ./$file ~/P_DATA
done


### (9) Make a tar of the files in P_DATA - call it pdata.tar
tar cf ~/pdata.tar ~/P_DATA


### (10) Compress pdata.tar
gzip -f ~/pdata.tar 



