# Problem Description
#
# Given two DNA strings "s" and "t" of equal length,
# (both not exceeding 1 kilo basepair (kbp))
# return the number of corresponding alignment mismatches.
# (Number of corresponding alignment mismatches aka "Hamming distance")

# Program Design Plan
#
# The program reads the two DNA sequences into two separate
# strings.
# Then, loop through the string and compare each corresponding
# indice's values. If they are not equal then increment
# the running count of number of mismatches. 

# I'm not sure how to read in the input data file and distinguish
# between the two DNA sequences, so I'm going to implement user
# input and copy+paste the two DNA sequences into the program 
# console.

seq_one = input("Enter the first DNA sequence: ")
seq_two = input("Enter the second DNA sequence: ")

num_mismatches = 0
for i in range(len(seq_one)):
    if seq_one[i] != seq_two[i]:
        num_mismatches += 1

print(f"The number of mismatches found is:---> {num_mismatches}")