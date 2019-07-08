def lis(_list, last=None):
    n = len(_list)
    if n == 0:
        return 0
    if n == 1:
        if last == None or last < _list[0]:
            return 1
        else:
            return 0

    l = []
    for i in range(1, n):
        i1, i2 = _list[i-1], _list[i]
        if i1 < i2:
            if last == None or last < i1: 
                l.append(1 + lis( _list[i:], i1))
        else:
            l.append(lis( [i1] + _list[i+1:] ))
    return max(l)

print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
