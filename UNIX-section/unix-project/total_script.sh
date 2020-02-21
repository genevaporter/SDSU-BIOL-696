#!/bin/bash

### To make executable: 
### > chmod +x total_script/sh 
### > ./total_script.sh
### If the .sh fils is in a PATH directory, no need for "./"

cd ~/REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/
bash Porter_project_bash.sh
cd ~/RAW_DATA
bash Porter_fasta_script.sh
cd ..
bash Porter_backup.sh P_DATA
bash Porter_backup.sh RAW_DATA
bash Porter_backup.sh RESULTS
