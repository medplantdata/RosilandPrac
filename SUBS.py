string ='GATATATGCATATACTT' 
substring ='ATAT'

pos = []

for k in range(len(string) - len(substring) + 1):
    checkString = string[k:k+len(substring)]
    if substring == checkString:
        pos.append(k+1)

print(pos)