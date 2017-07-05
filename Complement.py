"""
COMPLEMENT STRING
"""
#!/user/bin/pytho
def complement(sequence):
    "This is a sub function of REVERSE COMPLEMENT"
    "For more help please seek help on reversecomplement"
    basecomplement = {'A':'T','C':'G','G':'C','T':'A'}
    letters = list(sequence)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)
