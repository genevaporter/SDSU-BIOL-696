# I used OOP and dataframes to complete this assignemnt. The code is not very
# elegant, and quite a bit longer than necesscary, but I just wanted to practice
# OOP and dataframes a bit more. Hope that's alright. 

# Class from old code from the python OOP project

class Seq:
    
    def __init__ (self, sequence, species):
        self.sequence = sequence.strip().upper()
        self.species = species
    
    def find_kmers(self, string, k):    
        kmers = []
        n = len(string)
        for i in range(0, n-k+1):
            kmers.append(string[i:i+k])
        return kmers

    
    
# Assigning each bug to it's own object

exec(open("./kmer-data.py").read())

bug1 = Seq(data['bug1'], 'Bug 1')
bug1.kmers04 = bug1.find_kmers(bug1.sequence, 4)
bug1.kmers10 = bug1.find_kmers(bug1.sequence, 10)

bug2 = Seq(data['bug2'], 'Bug 2')
bug2.kmers04 = bug2.find_kmers(bug2.sequence, 4)
bug2.kmers10 = bug2.find_kmers(bug2.sequence, 10)

bug3 = Seq(data['bug3'], 'Bug 3')
bug3.kmers04 = bug3.find_kmers(bug3.sequence, 4)
bug3.kmers10 = bug3.find_kmers(bug3.sequence, 10)

bug4 = Seq(data['bug4'], 'Bug 4')
bug4.kmers04 = bug4.find_kmers(bug4.sequence, 4)
bug4.kmers10 = bug4.find_kmers(bug4.sequence, 10)



# Creating comparison test bug

query = "GCTTTTCATTCTGACTGCAACGGGCAATATGTCTCCGTTATCGATCCGGTCG" +\
        "AAAAACTGCTGGCAGTGGGGCATTACCTCGAATCTACCGTCGATATTGCTGA" +\
        "GGTGCCCGATGCGAGGTTGTTGAAGTCGATGTCCTACCAGGAAGCGATGGAG" +\
        "CTTTCCTACTTCGGCGCTGAAATCCTCAAGCACCAGGTACGCTCATTGGTGC" +\
        "CAGCCGTGATGAAGACGAATTACCGGTCAAGGGCATTTCCAATCTGAATAAC" +\
        "ATGGCAATGTTCAGCGTTTCTGGTCCAGGGATGAAAGGAATGGTCGGC"

testbug = Seq(query, 'Test Bug')
testbug.kmers04 = testbug.find_kmers(testbug.sequence, 4)
testbug.kmers10 = testbug.find_kmers(testbug.sequence, 10)



# Finding similarities

bug1.comp04 = len(set(bug1.kmers04) & set(testbug.kmers04))
bug1.comp10 = len(set(bug1.kmers10) & set(testbug.kmers10))

bug2.comp04 = len(set(bug2.kmers04) & set(testbug.kmers04))
bug2.comp10 = len(set(bug2.kmers10) & set(testbug.kmers10))

bug3.comp04 = len(set(bug3.kmers04) & set(testbug.kmers04))
bug3.comp10 = len(set(bug3.kmers10) & set(testbug.kmers10))

bug4.comp04 = len(set(bug4.kmers04) & set(testbug.kmers04))
bug4.comp10 = len(set(bug4.kmers10) & set(testbug.kmers10))



# Formatting output

import array
import pandas

CompArray = [[4 , bug1.species, '--->', bug1.comp04], \
             [4 , bug2.species, '--->', bug2.comp04], \
             [4 , bug3.species, '--->', bug3.comp04], \
             [4 , bug4.species, '--->', bug4.comp04], \
             [10, bug1.species, '--->', bug1.comp10], \
             [10, bug2.species, '--->', bug2.comp10], \
             [10, bug4.species, '--->', bug3.comp10], \
             [10, bug4.species, '--->', bug4.comp10]]

CompDf = pandas.DataFrame(CompArray, \
         columns = ['Length', 'Species', '', 'Results'], \
         index = ['', '', '', '', '', '', '', '', ])

CompDf = CompDf.sort_values(by = 'Results', ascending = False)
CompDf = CompDf.sort_values(by = 'Length')
CompDf