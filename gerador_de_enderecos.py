import random
import sys
import struct
params = sys.argv[1].split(':')
print(params)
numEnd = int(params[0])
valMax = int(params[1])
arqName = sys.argv[2]
arq = open(arqName, 'wb')
for i in range(int(numEnd)):
    j = random.randint(0, int(valMax))
    print(j)
    arq.write(struct.pack('I', j))
arq.close()
