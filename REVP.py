

#///////////////////////////////////////////////////////////////////////////////

#doesnt work

#///////////////////////////////////////////////////////////////////////////////



DNAseq = 'TCAATGCATGCGGGTCTATATGCAT'
revSeq = DNAseq[::-1]
revComp = ''

for k in range(len(revSeq)):
    if revSeq[k] == 'A':
        revComp = revComp[:k] + 'T' 
    elif revSeq[k] == 'T':
        revComp = revComp[:k] + 'A' 
    elif revSeq[k] == 'C':
        revSeq = revComp[:k] + 'G' 
    elif revSeq[k] == 'G':
        revComp = revComp[:k] + 'C' 

output =''
pos = 0
length = 0

while revComp != '':
    for k in range(4,len(revComp)+1):
        checkseq = revComp[0:k]
        if checkseq in DNAseq:
            length = k
            pos = DNAseq.index(checkseq) +1
    output += str(pos) + ' ' + str(length) + '\n'
    revComp = revComp[:length-1]

print(output)