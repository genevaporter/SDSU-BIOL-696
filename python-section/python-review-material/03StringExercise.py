# Here is a bad bit of DNA (actually RNA) that your lazy lab technician
# typed in the computer and you need to clean it up.

bad_dna="\n\t  \t  aGccUgUUa GUUAccac:++C\n   "

print (bad_dna)  #Dumps to screen when you run this script


# What do the following methods do to bad_dna? Use the print funciton
# after each command to see what happened
#
bad_dna=bad_dna.upper()
bad_dna=bad_dna.strip()
bad_dna=bad_dna.replace("+","-")
print(bad_dna)



#####
#EXERCISE
#####
#When finished, good_dna should "AGCCTGTTAGTTACCACC"

# Change bad_dna to something better. Use the following
# protocol to fix up bad_dna with the string functions:

# (1) Make sequence uppercase (Uncomment the next two lines.)
# good_dna=bad_dna.upper()
# print (good_dna)

# (2) Then strip off the white space at the beginnings and end of
#     the sequence
# (3) Replace the "+" with "-"
# (4) Replace the ":" with "-"
# (5) Replace the " " with ""
# (6) Finally, replace the "U" with "T" to make it DNA and save the final
#     clean string to the variable named good_dna

good_dna=""
print(good_dna)


