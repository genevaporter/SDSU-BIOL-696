## Step1: Rename this file YourLastName_kmer.py

##GOALS: Using kmer comparisons as an alignment-free method for sequence
##  matching and comparing the effects of kmer length.
##
## You will write a script that uses kmers to determine which
##  of 4 sequences is the best match to your query sequence below.
##  The 4 sequences are given as a dictionary in a separate file.

##When finished, your program should compare the sequences using two kmer
##  lengths: 4 and 10. The program should then print the results
##  in the format below, with the name of the bug and the match score.
##  (I made up the scores for this example).
##  The results do not have to be sorted (looks nicer though).

"""
Results for k-mer length 4:
bug3	300
bug4	200
bug1	100
bug2	10
Results for k-mer length 10:
bug1	200
bug2	150
bug3	10
bug4	0
"""

##The exec function is the way python 3 executes code from a separate file
##  (Replacement for execfile function in python 2). The code below executes
##  file "kmer-data.py" which contains a dictionary with 4 DNA sequencs as
##  key:value pairs of DNA sequences for bug1, bug2, bug3, bug4 

exec(open("./kmer-data.py").read())

##Use the find_kmers function below and the set function to determine the
##  bug that has the closest match to query. This type of kmer approach
##  is considered an "alignment free" method because we only care about the
##  shared kmers and they can be in any order.

query="GCTTTTCATTCTGACTGCAACGGGCAATATGTCTCCGTTATCGATCCGGTCGAAAAACTGCTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCTGAGGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAGCTTTCCTACTTCGGCGCTGAAATCCTCAAGCACCAGGTACGCTCATTGGTGCCAGCCGTGATGAAGACGAATTACCGGTCAAGGGCATTTCCAATCTGAATAACATGGCAATGTTCAGCGTTTCTGGTCCAGGGATGAAAGGAATGGTCGGC"


def find_kmers(string, k):
    
      kmers = []
      n = len(string)

      for i in range(0, n-k+1):
           kmers.append(string[i:i+k])

      return kmers  #A list of all kmers of length k

#Two different kmer lengths

k4=4
k10=10

##How to compare the union of two lists in python using the set function.
##  Below the variable 'comp' is a list of common elements form list 1 and 2

#comp=set(list1) & set(list2)
#x=len(comp)

## If these two lists have 5 elements in common, then x will equal 5
##Here is a bit of code I wrote to do the comparisons using our data

#kmatch=set(find_kmers(query,k)) & set(find_kmers(data[bug],k))
#result=len(kmatch)


            
