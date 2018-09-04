def subsets_of_set(s, out=None):
    if out == None: out = []
    
    if len(s):
        if s not in out:
            out.append(s)        
            if 1 < len(s):
                subsets_of_set(s[:-1], out)
                subsets_of_set(s[1:] + [s[0]], out)

    return out

print(subsets_of_set(['a','b','c']))
print(subsets_of_set(['e','f','g','h']))
