#!/user/bin/python
"""
LIBRARIES
"""
import random
import sys
"""
FUNCTION FILES
"""
import GC_Per_Cal
import Cannonical
import Sto_Codons
import Rev_Compl
"""
FUNCTIONS FROM FILES
"""
from GC_Per_Cal import GC_Per_Cal
from Cannonical import cannonical_pos
from Sto_Codons import has_stop_codon
from Rev_Compl import reversecomplement

"""
CODE SEQUENCE
"""
file = open("DNAsequence.txt","r")
sequence = file.read()
file.close()

"""
GC PERCENTAGE CALCULATION
"""
GC_Per_Cal(sequence)

"""
CANNONICAL DONOR SITE DETECTION
"""
cannonical_pos(sequence)
print("Cannonical Donor Site positions detected and stored...")
"""
FINDING STOP CODON
"""

if (has_stop_codon(sequence)) :
    print("Input sequence has an in-frame stop codon")
else :
    print("Input sequence does not have an in-frame stop codon")

"""
REVERSE COMPLEMENT SEQUENCE
"""
#reversecomplement(sequence)

