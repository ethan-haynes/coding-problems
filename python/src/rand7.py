from random import random
from math import floor
def rand5():
    return int(floor(random() * 5) + 1)

def rand7():
    return rand5() + int(floor(random() * 2) + 1)

print(rand7())
