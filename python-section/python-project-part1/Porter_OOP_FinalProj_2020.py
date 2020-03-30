import re
import math

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

kyte_doolittle = {
    'A':1.8,  'C':2.5,  'D':-3.5, 'E':-3.5, 'F':2.8,
    'G':-0.4, 'H':-3.2, 'I':4.5,  'K':-3.9, 'L':3.8,
    'M':1.9,  'N':-3.5, 'P':-1.6, 'Q':-3.5, 'R':-4.5,
    'S':-0.8, 'T':-0.7, 'V':4.2,  'W':-0.9, 'Y':-1.3,
    'X':0}



class Seq:
    
    def __init__ (self, sequence, gene, species, kmers=''):
        self.sequence = sequence.strip().upper()
        self.gene = gene
        self.species = species    
        self.kmers = []
    
    def __str__(self):
        return self.sequence
    
    def print_record(self):
        print(self.species +" "+ self.gene +" : "+ self.sequence)
    
    def make_kmers(self, subsequence_length = 3):
        self.kmers = []
        total_sequence_length = len(self.sequence)
        for x in range(total_sequence_length-subsequence_length+1):
            self.kmers.append(self.sequence[x])
            for y in range(1,subsequence_length):
                self.kmers[x] += self.sequence[x+y]
    
    def fasta(self):
        return ">" + self.species + " " + self.gene + "\n" + self.sequence
 

    
class DNA(Seq):
    
    def __init__(self, sequence, gene, species, gene_id, **kwargs):
        super().__init__(sequence, gene, species)
        self.sequence = re.sub('[^ATGCU]+', 'N', self.sequence)
        self.gene_id = gene_id
    
    def analysis(self):
        y = 0
        for x in self.sequence:
            if x == 'G' or x == 'C':
                y += 1
        return y
    
    def print_info(self):
        print(self.gene_id + " " + self.species +" "+ self.gene +" : "+ self.sequence)



class RNA(DNA):
    
    def __init__(self, sequence, gene, species, gene_id, codons='', **kwargs):
        super().__init__(sequence, gene, species, gene_id)
        self.sequence = re.sub('[T]', 'U', self.sequence)
        self.codons = []
        
    def make_codons(self):
        self.codons = []
        partition = math.floor(len(self.sequence)/3)
        for x in range(partition):
            self.codons.append(self.sequence[3*x])
            for y in range(1,3):
                self.codons[x] += self.sequence[3*x+y]
                
    def translate(self):
        translation = ''
        for x in range(len(self.codons)):
            if "N" in self.codons[x]:
                translation += "X"
            else:
                translation += standard_code[self.codons[x]]
        return translation



class Protein(Seq):
    
    def __init__(self, sequence, gene, species, kmers, counts='', **kwargs):
        super().__init__(sequence, gene, species, kmers)
        self.sequence = re.sub('[^A-Z]', 'X', self.sequence)
        self.counts = {}
        self.aa_counts = {'A':0,'C':0,'D':0,'E':0,'F':0,
                          'G':0,'H':0,'I':0,'K':0,'L':0,
                          'M':0,'N':0,'P':0,'Q':0,'R':0,
                          'S':0,'T':0,'V':0,'W':0,'Y':0,
                          'X' :0}
        # Note: The best way I could get my code to work was to
        # eliminate "U" as a definition in aa_counts, since it 
        # does not exist in the kyte_doolittle dictionary. I Hope 
        # this is correct.
        
    def tabulate_amino_acids(self):
        for x in self.sequence:
            self.aa_counts[x] += 1
        return 0
    
    def total_hydro(self):
        total = 0
        for x in self.aa_counts:
            total += self.aa_counts[x] * kyte_doolittle[x]
        return total
    
    def hydro_scan(self):
        if self.kmers == []:
            self.make_kmers(5)
        hydro_list = []
        kmer_length = len(self.kmers[0])
        for x in self.kmers:
            hydro_list.append(0)
            kmer_index = self.kmers.index(x)
            for y in x:
                hydro_list[kmer_index] += kyte_doolittle[y]/kmer_length          
        return hydro_list
    
    

    







