def subset(s, n, arr=[]):
    def sub(s, n, arr=[]):
        if n:
            return sub(s[:n-1] + s[n:], n-1, arr + [s])
        else: return arr
    if n:
        return subset([s[-1]] + s[:-1], n-1, arr + sub(s, len(s)))
    else: return arr

print(subset([1,2,3], 3))
