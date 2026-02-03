import numpy as np

textfile = r"C:\Users\School\Downloads\rosalind_cons (4).txt"
with open(textfile) as f:
   fasta = f.readlines()

testFASTA = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""


seqs = []
with open(textfile) as f:
    current = []
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current:
                seqs.append("".join(current))  # finish previous sequence
                current = []
        else:
            current.append(line)               # accumulate sequence lines
    if current:
        seqs.append("".join(current))

pyMatrix = [list(s) for s in seqs]

matrix = np.array(pyMatrix)
countDic = {'A':[], 'C':[], 'G':[], 'T':[]}
consenus = ''

for k in range(len(matrix[0])):
    Acount = 0
    Ccount = 0
    Gcount = 0
    Tcount = 0
    for j in range(matrix.shape[0]):
        if matrix[j][k] == 'A':
            Acount += 1
        elif matrix[j][k] == 'C':
            Ccount += 1
        elif matrix[j][k] == 'G':
            Gcount += 1
        elif matrix[j][k] == 'T':
            Tcount += 1
        
    maxCount = max(Acount, Ccount, Gcount, Tcount)
    if maxCount == Acount:
        consenus += 'A'
    elif maxCount == Ccount:
        consenus += 'C'
    elif maxCount == Gcount:
        consenus += 'G'
    elif maxCount == Tcount:
        consenus += 'T'

    countDic['A'].append(Acount)
    countDic['C'].append(Ccount)
    countDic['G'].append(Gcount)
    countDic['T'].append(Tcount)    



print(consenus + '\n' + 'A: ' + ' '.join(map(str, countDic['A'])) + '\n' + 'C: ' + ' '.join(map(str, countDic['C'])) + '\n' + 'G: ' + ' '.join(map(str, countDic['G'])) + '\n' + 'T: ' + ' '.join(map(str, countDic['T'])))