DNAstringIN = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
numA = 0
numT = 0
numC = 0    
numG = 0

for k in range(len(DNAstringIN)):
    if DNAstringIN[k] == "A":
        numA += 1
    elif DNAstringIN[k] == "T":
        numT += 1
    elif DNAstringIN[k] == "C":
        numC += 1
    elif DNAstringIN[k] == "G":
        numG += 1

print(str(numA) + " " + str(numC) + " " + str(numG) + " " + str(numT))