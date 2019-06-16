def lrs(s : str) -> str:
    
    def sub_check(sub : str) -> int:
        c = s.count(sub)
        if c > 1 and len(sub) and len([ _ for _ in s.split(sub)[1:-1] if _ ]) == 0:
            return c * len(sub)
        return -1

    def _lrs(sub : str) -> str:
        if len(sub):
            return max(_lrs(sub[1:]), _lrs(sub[:-1]), sub, key=sub_check) 
        return ""

    return _lrs(s)

print(lrs("676"))
print(lrs("6667"))
print(lrs("814414414414414"))
