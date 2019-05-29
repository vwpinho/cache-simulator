'''
Arguments are read as strings
The first arg is the name of the program argv[0]
The second arg is the configurations separated by : argv[1]
The third arg is the name of the binary file with the addresses argv[2]

Cache addressed by byte
Addresses with 32 bits
'''
# imports
from cache import Cache
import sys

# read arguments
if len(sys.argv) == 2:
    config = [256, 4, 1, 'r']
    inFile = sys.argv[1]
else:
    config = sys.argv[1].split(':')
    inFile = sys.argv[2]

# read the binary file
arq = open(inFile, 'rb')
b = arq.readlines()
acessos = str(b[0]).split('0b')[1:]

# cache init with the params
c = Cache(int(config[0]), int(config[1]), int(config[2]), config[3])

# simulation
for i in range(len(acessos)):
    if i == len(acessos)-1:
        c.write(acessos[i][:len(acessos[i])-1])
    else:
        c.write(acessos[i])

# simulation results
print('MissComp {}'.format(c.missComp))
print('MissConf {}'.format(c.missConf))
print('MissCap {}'.format(c.missCap))
print('Hits {}'.format(c.hits))

# closing arq
arq.close()
