def substring(s, sub):
    mem = ''
    for i, val in enumerate(s):
        if val == sub[len(mem)]:
            mem += val
        else:
            mem = ''
            if val == sub[len(mem)]:
                mem += val
        if mem == sub:
            return True

    return False

print(substring('hitherebob', 'here'))
print(substring('apppppppples', 'ple'))
print(substring('apples', 'azple'))
print(substring('aaaaaa', 'a'))
