def group_anagrams(strs):
    groups = {}
    
    n = len(strs)

    for i in range(n):
        s = strs[i]
        _s = "".join(
            sorted(s)
        )
        if _s in groups:
            groups[_s].append(s)
        else:
            groups[_s] = [s]

    return groups.values()

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
