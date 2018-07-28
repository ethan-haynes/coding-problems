def permuations(s, n=None):
    if n == None: n = len(s)
    trim = lambda s: len(s) and [s] + (trim(s[:-1]) or [])
    if n > 0:
        return trim(s) + (permuations(s[-1:] + s[:-1], n-1) or [])

print(permuations(''))
