#!/bin/bash

### (1) Check if the directory BACKUP_FILES exits in your home directory. If it does 
###     not exist, create the directory and echo "Created BACKUP_FILES in $HOME 
###     directory." If directory exists, echo "Directory $HOME/BACKUP_FILES exists."
if [ -d "$HOME/BACKUP_FILES/" ] 
then
    echo "Directory $HOME/BACKUP_FILES exists." 
else
    echo "Directory $HOME/BACKUP_FILES does not exist."
    mkdir $HOME/BACKUP_FILES/ 
    echo "Created BACKUP_FILES in $HOME/ directory"
fi


### (2) Write a for loop that copies all the files of a directory into BACKUP_FILES
###  The directory needs to be the first option after the script (see above).
for x in $1/*
do
    cp $x $HOME/BACKUP_FILES
    echo "$x copied to $HOME/BACKUP_FILES"
done


### (3) Create a function called print_info that
###     (a) Uses the ls command to output all the file information (option -al)
###         in $HOME/BACKUP_FILES to the screen.
###     (b) Runs the disk usage command on the same file to report total
###         kilobytes of all the files in the directory.
###     (c) Then run print_info
print_info () {
    ls -al $HOME/BACKUP_FILES
    du -sh $HOME/BACKUP_FILES
}
print_info 



