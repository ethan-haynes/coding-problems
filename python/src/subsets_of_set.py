def subsets_of_set(s, out=None, memo=None):
    if out == None: out, memo = [], set()
    l = len(s)
    if l:
        v = s[0] + str(l)
        if v not in memo:
            memo.add(v), out.append(s)
            if 1 < l:
                subsets_of_set(s[:-1], out, memo)
                subsets_of_set(s[1:] + [s[0]], out, memo)

    return out

print(subsets_of_set(['a','b','c']))
print(subsets_of_set(['e','f','g','h']))
print(subsets_of_set(['i','j','k','l','m','n','o']))
