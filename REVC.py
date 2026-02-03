inputDNA = 'AAAACCCGGT' 

reverseDNA = inputDNA[::-1]
outPutRev = ''

for k in range(len(reverseDNA)):
    if reverseDNA[k] == "A":
        outPutRev += "T"
    elif reverseDNA[k] == "T":
        outPutRev += "A"    
    elif reverseDNA[k] == "C":
        outPutRev += "G"
    elif reverseDNA[k] == "G":
        outPutRev += "C"

print(outPutRev)
