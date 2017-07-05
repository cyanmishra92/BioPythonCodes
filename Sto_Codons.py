"""
STOP CODON FINDING
"""
#!/user/bin/python
def has_stop_codon(dna,frame=0) :
    "This function checks whether there are in-frame stop codons in a given sequrnce"
    "And if available,list the stop codons in a file called stop_codon.txt"
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame,len(dna),3) :
        codon = dna[i:i+3].lower()
        if codon in stop_codons :
            stop_codon_found = True
            break
    return stop_codon_found
