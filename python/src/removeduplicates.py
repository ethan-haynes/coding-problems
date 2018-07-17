def removeduplicates(s):
    letters = set()
    out = ''
    for i in s:
        if i not in letters:
            out += i
            letters.add(i)

    return out

print(removeduplicates('abcdef'))
print(removeduplicates('abcdeeeef'))
