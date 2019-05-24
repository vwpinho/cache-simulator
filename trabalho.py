from cache import Cache
from math import log2
'''
Argumentos sao lidos como string
Da maneira do professor teremos como primeira entrada o nome do programa argv[0]
Como segunda entrada as configuracoes separadas por : argv[1]
E na terceira o nome do arquivo de acessos argv[2]
A cada 8 bytes um inteiro e escrito
arq.read(1) le 1 byte
'''
import sys
import struct
import array
import math

''' 
Testes
print(len(sys.argv))
print(type(sys.argv[2]))
print(sys.argv[1].split(':')) 
'''
'''
    Cache enderecada a byte
    End de 32 bits



'''
print(len(sys.argv))
if len(sys.argv) == 2:
    config = [256, 4, 1]
    inFile = sys.argv[1]
else:
    config = sys.argv[1].split(':')
    inFile = sys.argv[2]
acessos = []
#print(config)
#print(inFile)
# arq = open('teste.dat', 'wb')
#  *************  FUNCIONA POREM GAMBIARRA  ***********
arq = open(inFile, 'rb')
b = arq.read(4)
#s = str(bin(int(struct.unpack('I', b)[0] / 16777216)))[2:]
#print(s)

while b:
    #   print(struct.unpack('I', b)[0] / 16777216)
    s = bin((int(struct.unpack('I', b)[0] / 16777216)))[2:]
    acessos.append(s)
    b = arq.read(4)
#print(type(acessos[1]))
#print(len(acessos))
#ind = int(str(acessos[1])[10:20], 2)
#print(ind)
c = Cache(int(config[0]), int(config[1]), int(config[2]))
for i in range(len(acessos)):
    c.write(int(acessos[i]))
print('MissComp {}'.format(c.missComp))
print('MissConf {}'.format(c.missConf))
print('MissCap {}'.format(c.missCap))
print('Hits {}'.format(c.hits))

arq.close()
