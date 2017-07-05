"""
REVERSE COMPLEMENT
"""
#!/user/bin/python
import Reverse_String
import Complement

from Reverse_String import reverse_string
from Complement import complement

def reversecomplement(sequence) :
    "This function reads a DNA data file and finds its reverse-complement."
    "Reverse-complement of a data gives the sequence of the opposite stand."
    "Usually a DNA data of FASTA file contains data from a single stand."
    "But for pattern recognition and error reduction it is better to have the"
    "data from both the stands of a DNA. This function is very important in"
    "terms of pattern recognition of a DNA data"

    "Reverse complement of a data is usually done in two steps: "
    "1. Reversing the string."
    "2. complementing the string."
    "In REVERSING the original strand is reverse ordered."
    "In complement the complement of each component of the reversed string"
    "is put in its postion. The complement order is:"
    "A - T"
    "C - G"
    "T - A"
    "G - C"

    reverse = reverse_string(sequence)
    rev_complemet = complement(reverse)
    #return rev_complement
    file = open("Rev_Compl.txt", "w")
    file.write(rev_complement)
    file.close()
