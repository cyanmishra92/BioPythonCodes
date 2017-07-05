"""
GC PERCENTAGE CALCULATION
"""
#!/user/bin/python
def GC_Per_Cal(sequence) :
    "This function reads the DNA file to calculate the GC% content"
    gc_percentage = (sequence.count('G')+sequence.count('C'))/len(sequence)*100
    print("The GC percentage of the gene is %2.8f" %gc_percentage)
