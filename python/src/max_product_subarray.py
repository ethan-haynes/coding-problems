from functools import reduce

def mps(_list):
    n = len(_list)
    if n == 0:
        return []
    if n == 1:
        return [_list]
    
    l = []
    for i in range(n):
        for j in range(n,i,-1):
            l.append(reduce(lambda a,b: a*b, _list[i:j]))
    return max(l)

print(mps([2, 3, -2, 4]))
