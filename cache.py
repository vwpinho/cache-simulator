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

        for i in range(assoc):
            self.cache.insert(i, [])
            for j in range(nsets):
                self.cache[i].insert(j, Bloco())
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
            ind = 0;
        else:
            ind = int(str(end)[tamtag:(tamtag + int(math.log2(self.nsets)))], 2)
        for i in range(self.assoc):
            b = self.cache[i].pop(ind)
            if b.val == 0:
                self.missComp += 1
                b.write(tag)
                self.cache[i].insert(ind, b)
                self.fifo.append(i)
                self.lru.append(i)
                write = True
                break
            else:
                if b.tag == tag:
                    self.hits += 1
                    self.cache[i].insert(ind, b)
                    self.lru.remove(i)
                    self.lru.append(i)
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
                aux = self.lru[0]
                b = self.cache[self.lru[0]].pop(ind)
                b.write(tag)
                self.cache[self.lru[0]].insert(ind, b)
                self.lru.remove(self.lru[0])
                self.lru.append(aux)
            if self.pol == 'f':
                aux = self.fifo[0]
                b = self.cache[self.fifo[0]].pop(ind)
                b.write(tag)
                self.cache[self.fifo[0]].insert(ind, b)
                self.fifo.remove(self.fifo[0])
                self.fifo.append(aux)
            if self.pol == 'r':
                ri = random.randint(0, (self.assoc - 1))
                b = self.cache[ri].pop(ind)
                b.write(tag)
                self.cache[ri].insert(ind, b)

