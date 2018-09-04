def subsets_of_set(s):
    out = []
    
    def __subs(s):
        if len(s) == 0: return
        
        if s not in out:
            out.append(s)        
            if 1 < len(s):
                __subs(s[:-1])
                __subs(s[1:] + [s[0]])
    
    __subs(s)

    return out

print(subsets_of_set(['a','b','c']))
