"""
CANNONICAL DONOR SITE DETECTION
"""
#!/user/bin/python
def cannonical_pos(sequence) :
    "This function reads the DNA sequence file from the system"
    "And it detects the cannonocal donor sites and stores them in CANNONICAL_DONOR_SITE.txt "
    can_list = []
    pos = sequence.find('GT',0)
    while pos >=0 :
        can_list.append(pos)
        pos = sequence.find('GT',pos+1)
    can_list = str(can_list)
    file_can = open("CANNONICAL_DONOR_SITE.txt", "w")
    file_can.write("Donor splice site candidate at the following positions:\n")
    file_can.write(can_list)
    file_can.close()
