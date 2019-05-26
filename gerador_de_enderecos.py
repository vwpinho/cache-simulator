import random
import sys
params = sys.argv[1].split(':')
print(params)
numEnd = int(params[0])
valMax = int(params[1])
arqName = sys.argv[2]
arq = open(arqName, 'wb')
for i in range(numEnd):
    arq.write(bin(random.randint(0, valMax)))
arq.close()
