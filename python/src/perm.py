def perm(L):
    size = len(L)
    if size == 0:
        return []
    if size == 1:
        return [L]

    l = []

    for i in range(size):
        m = L[i]
        r = L[:i] + L[i+1:]

        for p in perm(r):
            l.append([m] + p)
    
    return l

print(perm([1,2,3]))
