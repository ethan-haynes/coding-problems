from random import random
from math import log10
from time import time

def shuffle(pl):
    n = len(pl)
    rand_pl = list(pl)
    
    for _ in range(n):
        a, b = int(random() * n), int(random() * n)
        rand_pl[a], rand_pl[b] = rand_pl[b], rand_pl[a]

    return rand_pl


def shuffle2(pl):
    n = len(pl)
    rand_pl = pl[:]
    
    for _ in range(n):
        a, b = int(random() * n), int(random() * n)
        rand_pl[a], rand_pl[b] = rand_pl[b], rand_pl[a]

    return rand_pl

def shuffle3(pl):
    n = len(pl)
    d = int(log10(n))
    
    for _ in range(n//d):
        a, b = int(random() * n), int(random() * n)
        pl[a], pl[b] = pl[b], pl[a]

    return pl

pl = list(range(10**5))

now = time()
shuffle(pl) 
print((time() - now))

now = time()
shuffle2(pl) 
print((time() - now))

now = time()
shuffle3(pl) 
print((time() - now))
