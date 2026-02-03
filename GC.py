def countGC(seq):
    count = seq.count('G') + seq.count('C')
    return (count / len(seq)) * 100

inputFASTA = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"""

dicFasta = dict(seq.split('\n') for seq in inputFASTA.strip().split('\n>'))
bigSeq =''
bigGC = 0

for header, seq in dicFasta.items():
    gc = countGC(seq)
    if gc > bigGC:
        bigGC = gc
        bigSeq = header
print(bigSeq + ' ' + str(bigGC))