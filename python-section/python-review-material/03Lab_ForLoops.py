#-------------------------------------------------------------------------------
#PYTHON LAB 3
#-------------------------------------------------------------------------------
import random

print("\n########## PART 1 ##########\n")
#PART 1 - STRING LOOPING & COUNTING

#(1) Use a "for" loop to iterate through the DNA sequence.
#(2) Count the number of G's and C's in the DNA sequence.
#(3) Print the number of G's and C's in the DNA sequence.

#DATASET FOR PART 1: try each of thes options
test_dna="GACCTTTAC"
#test_dna="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"

#== PART 1 ==



#-------------------------------------------------------------------------------
print("\n########## PART 2 ##########\n")

#PART 2 - CLEAN the Sequence first then calculate the percentage G and C

nasty_dna="\n AgGctgTtgC \t\n"

# (1) Clean the DNA sequence.
# (2) Use a "for" loop to iterate through the DNA sequence.
# (3) Count the number of G's and C's in the DNA sequence.
# (4) Calculate the fraction (NOT PERCENT) of G's and C's in the DNA sequence. 
# (5) Print the percentage of G's and C's in the DNA sequence.

#To get percentage divide the count of G and C by the total length of the DNA!
#For example: len(clean_dna)


#== PART 2 ==



#-------------------------------------------------------------------------------
print("\n########## PART 3 ##########\n")

#PART 3 - CHARACTER CLASSIFICATION

dna="AAGGTTCCCCG"*10

# (1) Count the number of each type of base in the DNA sequence.
# (2) Return the counts of each type of base in the DNA sequence.
# (3) Also print out a table of the counts as shown below.

#== PART 3 ==



#The table should look like this:
#   A   9
#   T	10
#   G	12
#   C	7

#-------------------------------------------------------------------------------
print("\n########## PART 4 ##########\n")

#PART 4 - Using range and random


#Use the random.shuffle function to make and print 10 random lists of names.

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print(names) #prints the unshuffled names

#== PART 4 ==


#-------------------------------------------------------------------------------
print("\n########## PART 5 ##########\n")

#PART 5 - Write everthing to a file!!

"""
For this last part, write all your results to a file called: YourName03Lab.txt
YourName should be changed to your name of course.

How to do this? It's easy!
(1) Put this code at the top of the file:
outfile=open('YourName03Lab.txt','w')

(2) After each print statement, add a line to write data to a file:

print(names)
out=str(names) # You can only write strings to a file!
outfile.write(out)

(3) At the end of this file put this:

outfile.close()

"""


