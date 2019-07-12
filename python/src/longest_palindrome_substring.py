def lps(s):
    n = len(s)
    l = ""
    for i in range(n):
        for j in range(i+1,n+1):
            sub = s[i:j]
            if len(sub) > len(l) and sub == sub[::-1]:
                l = sub
    return l

print(lps('abaabc'))
