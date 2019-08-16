#! /usr/bin/env python3

import random
import itertools

def einzweidrei(rep=13):
    rep = int(rep)
    def letter2num(word='ein', digit=1):
        digit = str(digit)
        res = [word.replace(y, digit) for y in word]
        return(res)
    ein = letter2num('ein', 1)
    zwei = letter2num('zwei', 2)
    drei = letter2num('drei', 3)
    def helper(num):
        l = [random.choice(num) for y in range(rep)]
        return(l)
    res = zip(helper(ein), helper(zwei), helper(drei))
    res = [item for sublist in res for item in sublist]
    #res = itertools.chain(*res)
    print(*res)

if __name__ == '__main__':
    import sys
    einzweidrei(sys.argv[1])
