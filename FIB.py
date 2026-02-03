numGenerations = 28
numLitter = 2

fibSeq = [1,1]

for k in range (2, numGenerations):
    fibSeq.append(fibSeq[k-1] + fibSeq[k-2] * numLitter)


print(fibSeq[-1])