inputDNA = 'GATGGAACTTGACTACGTAAATT'
outPutRNA = ''
for k in range(len(inputDNA)):
    if inputDNA[k] == "A":
        outPutRNA += "A"
    elif inputDNA[k] == "T":
        outPutRNA += "U"    
    elif inputDNA[k] == "C":
        outPutRNA += "C"
    elif inputDNA[k] == "G":
        outPutRNA += "G"

print(outPutRNA)