seq1 = "GAGCCTACTAACGGGAT"
seq2 = "CATCGTAATGACGGCCT"
hamm = 0
for k in range(len(seq1)):
    if seq1[k] != seq2[k]:
        hamm += 1
print(hamm)