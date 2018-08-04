
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

print(parenthesis(3))
