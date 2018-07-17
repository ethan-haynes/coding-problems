def is_anagram(s1='', s2=''):
    if s1 == s2: return True
    if len(s1) != len(s2): return False
    d1, d2 = {}, {}
    for i in range(len(s1)):
        if s1[i] in d1: d1[s1[i]].append(1)
        else: d1[s1[i]] = [1]

        if s2[i] in d2: d2[s2[i]].append(1)
        else: d2[s2[i]] = [1]
    return d1 == d2

print(is_anagram('abcde', 'edcba'))
print(is_anagram('abcdea', 'edcbaa'))
print(is_anagram('caaabaa', 'acaaaab'))
print(is_anagram('caaabaaC', 'acaCaaa'))
print(is_anagram('Characters', 'characters'))
