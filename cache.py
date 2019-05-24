from bloco import Bloco
from math import log2
import random

class Cache:
    wend = 32

    def __init__(self, nsets, bsize, assoc):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
        self.cache = []
        self.missComp = 0
        self.missCap = 0
        self.missConf = 0
        self.acess = 0
        self.hits = 0

        for i in range(assoc):
            self.cache.insert(i, [])
            for j in range(nsets):
                self.cache[i].insert(j, Bloco())

    def write(self, end):
        while len(str(end)) < 32:
            end = '0' + str(end)
        write = False
        tamtag = self.wend - int(log2(self.nsets)) - int(log2(self.bsize))
        tag = str(end)[0:tamtag]
        ind = int(str(end)[tamtag:(tamtag + int(log2(self.nsets)))], 2)
        for i in range(self.assoc):
            b = self.cache[i].pop(ind)

            if b.val == 0:
                self.missComp += 1
                b.write(tag)
                self.cache[i].insert(ind, b)
                write = True
                break
            else:
                if b.tag == tag:
                    self.hits += 1
                    self.cache[i].insert(ind, b)
                    write = True
                    break
                else:
                    self.cache[i].insert(ind, b)
        if not write:
            if self.nsets == 1:
                self.missCap += 1
            else:
                self.missConf += 1
            ri = random.randint(0, self.assoc)
            b = self.cache[ri].pop[ind]
            b.write(tag)
            self.cache[ri].insert(ind, b)







#        for i in range(len(Cache.cache)):

