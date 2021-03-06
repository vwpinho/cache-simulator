from bloco import Bloco

import random

class Cache:
    wend = 32

    def __init__(self, nsets, bsize, assoc, pol):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.cache = []
        self.fifo = []
        self.lru = []
        self.missComp = 0
        self.missCap = 0
        self.missConf = 0
        self.acess = 0
        self.hits = 0
        self.pol = pol
        for i in range(assoc):
            self.cache.insert(i, [])
            for j in range(nsets):
                self.cache[i].insert(j, Bloco())
        for i in range(0, self.nsets):
            self.fifo.insert(i, [])
            self.lru.insert(i, [])

    def write(self, end):
        import math

        while len(str(end)) < 32:
            end = '0' + str(end)
        write = False
        tamtag = self.wend - int(math.log2(self.nsets)) - int(math.log2(self.bsize))
        tag = str(end)[0:tamtag]
        if self.nsets == 1:
            ind = 0
        else:
            ind = int(str(end)[tamtag:(tamtag + int(math.log2(self.nsets)))], 2)
        for i in range(self.assoc):
            b = self.cache[i].pop(ind)
            if b.val == 0:
                self.missComp += 1
                b.write(tag)
                self.cache[i].insert(ind, b)
                self.fifo[ind].append(i)
                self.lru[ind].append(i)
                write = True
                break
            else:
                if b.tag == tag:
                    self.hits += 1
                    self.cache[i].insert(ind, b)
                    self.lru[ind].remove(i)
                    self.lru[ind].append(i)
                    write = True
                    break
                else:
                    self.cache[i].insert(ind, b)
        if not write:
            if self.nsets == 1:
                self.missCap += 1
            else:
                self.missConf += 1
            if self.pol == 'l':
                aux = self.lru[ind][0]
                b = self.cache[self.lru[ind][0]].pop(ind)
                b.write(tag)
                self.cache[self.lru[ind][0]].insert(ind, b)
                self.lru[ind].remove(self.lru[ind][0])
                self.lru[ind].append(aux)
            if self.pol == 'f':
                aux = self.fifo[ind][0]
                b = self.cache[self.fifo[ind][0]].pop(ind)
                b.write(tag)
                self.cache[self.fifo[ind][0]].insert(ind, b)
                self.fifo[ind].remove(self.fifo[ind][0])
                self.fifo[ind].append(aux)
            if self.pol == 'r':
                ri = random.randint(0, (self.assoc - 1))
                b = self.cache[ri].pop(ind)
                b.write(tag)
                self.cache[ri].insert(ind, b)

    def show_results(self):
        tot_miss = self.missComp + self.missCap + self.missConf
        tot_acess = self.missComp + self.missCap + self.missConf + self.hits
        print('{} simulation statistics {}'.format('*'*20, '*'*20))
        print('Misses Compulsorios:\t', end='')
        print('{}'.format(self.missComp).rjust(10))
        print('Misses de Conflito:\t', end='')
        print('{}'.format(self.missConf).rjust(10))
        print('Misses de Capacidade:\t', end='')
        print('{}'.format(self.missCap).rjust(10))
        print('Total de misses:\t', end='')
        print('{}'.format(tot_miss).rjust(10))
        print('Total de acessos:\t', end='')
        print('{}'.format(tot_acess).rjust(10))
        print('Hits:\t\t\t', end='')
        print('{}'.format(self.hits).rjust(10))
        print('Miss rate: \t\t', end='')
        print('{}'.format(tot_miss/tot_acess).rjust(10))

