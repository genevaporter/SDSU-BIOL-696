#LAST NAME: 
#----------------------------------------------------------------------------
#PYTHON LAB 2: Conditionals
#----------------------------------------------------------------------------
#NOTE:
#- First thing to do: Rename this file with your last name like this:

#Kelley02Lab_Conditionals.py

#- Read the instructions for each part CAREFULLY.
#- IN THE EXERCISES, USE THE VARIABLE NAMES INDICATED

#----------------------------------------------------------------------------
#== PART 1 ==

#Write a script below using if/elif/else that compares two variables, fx and fy.
#If the fx is greater than fy print "fx is da bomb."
#Else if fy is greater than fx print "No dude, fy is da bomb."
#Else print "They are both losers."


#Test different values of fx and fy
fx=9
fy=2
#fx=0.9
#fy=2.8
#fx=fy=0

#== PART 1 Answer ==



#---------------------------------------------------------------------------

#== PART 2 ==

#Write some code to test wether the length of the variable dna1
# is greater or equal to 10 bases (characters) long or less than 10 long.
# If greater or equal, print the sequence.
# Else print "Too Short!"

#Try it with different values of dna1:
dna1="GTAACAG"
#dna1="CAGATTAGGA"
#dna1="GGACAACCGATTACAGGATGCCG"

#== PART 2 Answer ==



#----------------------------------------------------------------------------

#== PART 3 ==
#Using the double equals sign!
#Write an if/then statement to check if the string seq  is a perfect match to
#EITHER of two sequences of human DNA: "GAATTC" or "CTTAAG"
#If it is a perfect match, print "MATCH". Else print ("FAIL")

#Test with different values of seq
seq="GAATTC"
#seq="CTTAAG"
#seq="ACACACAC"

#== PART 3 Answer ==


#-------------------------------------------------------------------------
#== PART 4 ==

"""
Write a script that does the following:

(1) Take in a sequence (mrna) as an argument and converts it to UPPER CASE.
(2) Extracts the first three letters from the sequence.
(3) Check if the first three letters is a start codon "AUG".
      If the sequence has a start codon print "Protein Sequence Found."
         and also print the sequence. print(mrna)
      Else if the start codon is NOT found, print "Protein Sequence not found."
"""

#Test the function with different values of mrna:
mrna="AUGGGAAAUUU"
#mrna="augggaaauuu"  #This has a lowercase 'aug' and should also print "Protein Sequence Found."
#mrna="GGGAAAAAG"

#== PART 4 Answer ==




