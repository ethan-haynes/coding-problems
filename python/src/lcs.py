def lcs(s1,s2):
    res, j, memo = ['',''], 0, set(s2)

    for i in range(len(s1)):
        if j == len(s2):
            j, res = 0, [max(res, key=len), '']
        if s1[i] in memo:
            while j < len(s2):
                if s1[i] == s2[j]:
                    res[1] += s1[i]
                    j += 1
                    break
                else: j += 1
    return res.pop()

print(lcs('AGGTAB', 'GXTXAYB'))
print(lcs('ABCDE', 'BCDEA'))
print(lcs('ABCDE', 'FGHIJ'))
