def fmp(arr):
    n = len(arr)
    i = bits = 0
    for i in arr:
        if i >= 0 and i < n+2:
            bits |= (1 << i)

    i = 1
    while i < n+2:
        if (bits >> i) & 1 == 0:
            return i
        i += 1

    return -1

print(fmp([1,2,3,4,5,6,7,8]))
print(fmp([1,2,4,5,6,7,8]))
print(fmp([-1,2,4,5,6,7,8]))
print(fmp([0,1,2,3,4,5,6,7,888888]))
