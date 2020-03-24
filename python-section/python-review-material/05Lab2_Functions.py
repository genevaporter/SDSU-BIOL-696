#Lab 5 part 2: Advanced Functions (Convert scripts to functions.)

"""
In this assignment, you will go back to your working code from 
previous assignments and converts your scripts to functions.

To begin, you can literally copy and paste the old code to this 
file then turn it into a working function. 

Test the functions with the values indicated and make sure
you get the results you expect to get.
"""

print("\n########## PART 1 ##########\n")

#PART 1 - Convert 03Lab part 2 to a function

#FUNCTION NAME: FractionGC
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Clean the DNA sequence.
#	    (2) Use a "for" loop to iterate through the DNA sequence.
#	    (3) Count the number of G's and C's in the DNA sequence.
#           (4) Calculate the fraction (NOT PERCENT) of G's and C's in the DNA sequence. 
#	    (5) Return the fraction of G's and C's in the DNA sequence.
#RETURN VALUES: The fraction of G's and C's in the DNA sequence. (A float)

test_seq1="GACCTTTAC"
test_seq2="GATCCTGGCTCAGGACGAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAGCGGTAAGGCCCTTCGGGGTACACGAGCGGCGAACGGGTGAGTAACACGTGGGTGATCTGGGGCCCCATCTA"


#== FUNCTION 1 ==

#EXAMPLE: 
#gc_content = fractionGC("\n AgGctgTtgC \t\n")
#print (gc_content)

#The function would return:
#   0.6

#Test the function with the sequences from the example.
#Test the function again with "test_seq1" and test_seq2" above.
#Return the "GC" content of "test_seq1" to "gc_content". 
#Test it again with "test_seq2". Print the value to check it.


print("\n########## PART 2 ##########\n")

#PART 2 - Convert 03Lab part 3 to a function

#FUNCTION NAME: count_DNA_bases
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Count the number of each type of base in the DNA sequence.
#           (2) Return the counts of each type of base in the DNA sequence.
#           (3) Also print out a table as shown below.
#RETURN VALUES: The counts of each type of base in the DNA sequence. (A tuple)
#                   [NOTE: Return the counts EXACTLY in this order: A's, T's, G's and C's.]
# Example tuples: my_tuple1=(x,y,z)  my_tuple2=(1,2,3,4)


#== FUNCTION 2 ==



#DATASET FOR PART 2:
test_dna1="AAGCTACGTGGGTGACTTTGCCGATTTAAGCCTGGGAA"

#EXAMPLE:
#DNAcounts=count_DNA_bases(test_dna1)
#print (DNAcounts)

#The function would print a table:
#   A   9
#   T	10
#   G	12
#   C	7

#The function would return:
#   (9, 10, 12, 7)


print("\n########## PART 3 ##########\n")

#Part 3 - Convert 03Lab part 4 to a function


#Use the random.shuffle function to make and print 10 random lists of names.

names=['Tara','Merkel','Bob','Dwight','Chrysanthemum','Tiny Tim','Boba Fett','Lando','Sgt. Rock','Beyonce']
print(names) #prints the unshuffled names

print("\n########## PART 3 ##########\n")

#PART 4 -  Convert 04Lab part 2 to a function


#FUNCTION NAME: codon_list
#PARAMETERS: 1 (A sequence)
#PURPOSE: The function should:
#   (1) Iterate through the sequence.
#   (2) Divide the sequence into sections of 3-base codons with NO OVERLAPPING.
#   (3) Add the codons to a list.
#   [NOTE: If a group is not 3 bases long, do not include it in the list.]
#   (4) Return the list.
#RETURN VALUES: A list of codons. (A list)

#== FUNCTION 1 ==



#EXAMPLE:
#dna1="AUGGGAAGC"
#codons=codon_list(dna1)
#print (codons)

#The function would return:
#   ["AUG","GGA","AGC"]


