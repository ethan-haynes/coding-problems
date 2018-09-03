def permuations(s, n=None):
    if n == None: n = len(s)
    rotate = lambda s, n: n > 0 and [s] + (rotate(s[:1] + s[2:] + s[1], n-1) or [])
    if n > 0:
        return (rotate(s, len(s)) or []) + (permuations(s[-1:] + s[:-1], n-1) or [])

print(permuations('abc'))



'''
abc -> acb -> bac -> bca -> cab -> cba
'''
def permutations2(s):
    out = {}

    def rotate(s):
        if s not in out:
            out[s] = 0
            rotate(s[1:] + s[0]), rotate(s[0] + s[2:] + s[1])

    rotate(s)

    return out.keys()

print(permutations2('abc'))
