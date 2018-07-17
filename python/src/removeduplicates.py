def rd1(s):
    letters = set()
    out = ''
    for i in s:
        if i not in letters:
            out += i
            letters.add(i)

    return out

print(rd1('abcdef'))
print(rd1('abcdeeeef'))

def rd2(s):
    return ''.join(list(set([ i for i in s])))

print(rd2('abcdef'))
print(rd2('abcdeeeef'))


def rd3(s):
    hash = {}
    for i in range(len(s)):
        if s[i] not in hash: hash[s[i]] = 1
    return ''.join(list(hash))

print(rd3('abcdef'))
print(rd3('abcdeeeef'))
