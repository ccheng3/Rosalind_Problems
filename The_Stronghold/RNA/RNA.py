# Problem Descripion
#
# Given a DNA string "t" having length at most 1000 nt,
# return the transcribed RNA string of "t", where the
# transcribed string is just the DNA string with all
# 'T' replaced with 'U'.

# Program Design Details
#
# Same plan as with DNA.py, will loop through
# DNA sequence and replace all "Thymine" occurrence

filename = "rosalind_rna.txt"
with open(filename) as fileobject:
    DNA_seq_string = fileobject.read()
    #print(DNA_seq_string)

# replace an occurrence of 'T' with 'U', and can specify
# the max number of replacements to do.
# ---> check replace() method if forget again.
#print(DNA_seq_string.replace('T','U'))

outputstring = DNA_seq_string.replace('T','U')
with open("RNA_output_file_two.txt", 'x') as ofobj:
    ofobj.write(outputstring)
