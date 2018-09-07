def num_distinct(s, t):
    if len(t):
        n = 0
        for i, v in enumerate(s):
            if v == t[0]:
                n += num_distinct(s[i+1:], t[1:])
    else: n = 1
    return n
