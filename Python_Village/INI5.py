# Problem Description and Solution Design Notes
#
# Given a file containing at most 1000 lines, 
# return a file containing all of the even-numbered lines from the 
# original file. (The lines in the file are assumed to be 1-based numbered)

# Solution Design
#
# First, read the file and store each line as an element in a list.
# Even-numbered lines in the original file will then become odd-numbered indices
# in the list. 
# Then, write the odd-numbered index elements of the list over to the output file.

filename = 'rosalind_ini5.txt' 
with open(filename) as fileobject:
    line_list = fileobject.readlines()

with open('INI5_outputfile.txt','w') as outputfile:
    for line in line_list:
        if (line_list.index(line) % 2 == 1):
            outputfile.write(line)    