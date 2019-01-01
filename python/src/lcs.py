def lcs(s1,s2):
    res = ['','']
    i, j = 0, 0
    memo = set(s2)

    while i < len(s1):
        if j == len(s2):
            j = 0
            res = [max(res, key=len), '']
        if s1[i] in memo:
            while j < len(s2):
                if s1[i] == s2[j]:
                    res[1] += s1[i]
                    j += 1
                    break
                else: j += 1
        i += 1    
    return res.pop()

print(lcs('AGGTAB', 'GXTXAYB'))
print(lcs('ABCDE', 'BCDEA'))
print(lcs('ABCDE', 'FGHIJ'))
