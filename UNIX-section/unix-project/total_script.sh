#!/bin/bash

cd
cd REPOSITORIES/SDSU-BIOL-696/UNIX-section/unix-project/
bash Porter_project_bash.sh
cd
cd biol696-1/RAW_DATA
bash Porter_fasta_script.sh
cd ..
bash Porter_backup.sh P_DATA
bash Porter_backup.sh RAW_DATA
bash Porter_backup.sh RESULTS
