
def parenthesis(n):
    out = set()
    def paren(n, arr):
        for i in range(n):
            end = arr.pop()
            arr = [end] + arr
            out.add(str(arr).replace(', ','').replace('[','(').replace(']',')')[1:-1])
        if n > 0 and len(arr) != 1:
            arr[0].append(arr.pop())
            end = arr.pop()
            arr = [end] + arr
            paren(n-1, arr)

    paren(n, [[] for _ in range(n)])
    return list(out)

def genParens(n):
    def gen(o, c, s):
        if not o and not c: return [s]
        if not o and c: return gen([], c[1:], s + c[-1])
        if len(o) == len(c): return gen(o[1:], c[::], s + o[-1])

        return gen(o[1:], c[::], s + o[-1]) + gen(o[::], c[1:], s + c[-1])
    return gen(['(' for _ in range(n)],[')' for _ in range(n)],'')

print(parenthesis(3))
print(genParens(3))
