#!/usr/bin/env python

import math

def flipInt(x):
    temp = math.fabs(x)
    length = math.ceil(math.log10(temp+1) or 1)
    sign = math.copysign(1, x)

    place = 10**(length-1)
    num = 0
    for i in range(0,length):
        num += temp%10 * place
        temp = math.floor(temp/10)
        place = math.floor(place/10)
    return int(num * sign)


def main():
    print(flipInt(123))
    print(flipInt(-321))


if __name__ == '__main__':
    main()
