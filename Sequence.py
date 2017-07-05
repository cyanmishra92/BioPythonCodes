#!/user/bin/python
import random
import sys

"""
SEQUENCE GENERATION
"""
length = input("Enter the length of the sequence:\n")
length = int(length)
dna = ['A','G','C','T']
sequence = ''
for i in range (length) :
    sequence += random.choice (dna)
"""
GENOME FILE GENERATION
"""
file = open("DNAsequence.txt", "w")
file.write(sequence)
file.close()
