# Problem Description
# 
# Given a DNA string "s" (that has at most a length of 1000 nt),
# return four integers counting the respective number of times
# that the 'A','C','G', and 'T' nucleotides occur in string "s".

# Program Design Details 
#
# The program design is simple:
# First, read the DNA sequence from the input file into a string. 
# Loop through the string and keep a running count of 
# each nucleotide occurence.
# Then report each nt total count. 

filename = "rosalind_rna.txt"

with open(filename) as fileobject:
    DNA_seq_string = fileobject.read()

# A, C, G, T is the order in the list
nucleotide_counts = [0,0,0,0]

for letter in DNA_seq_string:
    if letter == 'A':
        nucleotide_counts[0] += 1
    elif letter == 'C':
        nucleotide_counts[1] += 1
    elif letter == 'G':
        nucleotide_counts[2] += 1
    elif letter == 'T': 
        nucleotide_counts[3] += 1
    else:
        # catch all whitespace chars
        continue

print("Nucleotide counts have been calculated: \n")
print("A C G T\n")
print(nucleotide_counts)


# This is a simple O(N) solution since I have to 
# iterate through all of the chars in the string.


