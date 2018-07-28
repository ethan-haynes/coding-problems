def permuations(s):
    def reduce(s):
        if len(s):
            return [s] + (reduce(s[:-1]) or [])
    def rotate(s, n):
        if n > 0:
            return reduce(s) + (rotate(s[-1:] + s[:-1], n-1) or [])
    return rotate(s, len(s))

print(permuations('abc'))
