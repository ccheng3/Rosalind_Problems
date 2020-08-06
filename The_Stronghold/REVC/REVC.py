# Problem Description
#
# Given a DNA string "s" with a length at most of 1000 bp,
# return the reverse complement "s^c" of "s".

# Program Design Details
#
# This program breaks the problem down into two steps:
# First, reverse the elements of the string.
# Then, find and output the complement of that reversed string. 

# NOTE: the string reversal algo can be implemented iteratively
# and also recursively (review the Liang folder for code - i think
# it's on the T450.)

filename = 'rosalind_revc.txt'
with open(filename) as fileobject:
    input_DNA_seq = fileobject.read()

reversed_string = ''
for i in range(len(input_DNA_seq)):
    reversed_string += input_DNA_seq[len(input_DNA_seq)-1-i]

#print(reversed_string)

rev_comp_string = ""
for i in range(len(reversed_string)):
    if reversed_string[i] == 'A':
        rev_comp_string += 'T'
    elif reversed_string[i] == 'T':
        rev_comp_string += 'A'
    elif reversed_string[i] == 'G':
        rev_comp_string += 'C'
    elif reversed_string[i] == 'C':
        rev_comp_string += 'G'

#print(rev_comp_string)
output_filename = 'REVC_real_output_seq.txt'
with open(output_filename,'x') as ofobj:
    ofobj.write(rev_comp_string)
