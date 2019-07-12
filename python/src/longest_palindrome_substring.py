def lps(s):
    n = len(s)
    l = ""
    for i in range(n):
        for j in range(i+1,n+1):
            sub = s[i:j]
            if len(sub) > len(l) and sub == sub[::-1]:
                l = sub
    return l

def lps2(s):
    n = len(s)
    m = [[ 0 for i in range(n) ] for i in range(n) ]
    for i in range(n//2):
        for j in range(i+1,n+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                m[i][j-1] = len(sub)
    return m

def lps3(s):
    n = len(s)
    l = ""
    for i in range(n//2):
        for j in range(i+1,n+1):
            sub = s[i:j]
            if len(sub) > len(l) and sub == sub[::-1]:
                l = sub
    return l

print(lps('abaabc'))
print(lps2('abaabc'))
print(lps3('abaabc'))
