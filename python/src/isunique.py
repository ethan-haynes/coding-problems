"""
    implement algorithm to determine if string has all unique
    characters with no additional data structurs.
"""
def isunique(s):
    last = ''
    for i in sorted(s):
        if i == last: return False
        else: last = i
    return True

print(isunique('abcde'))
print(isunique('abcdee'))
print(isunique('aaaa'))

"""
    implement algorithm to determine if string has all unique
    characters with additional data structurs.
"""
def is_unique_with_dict(s):
    hash_table = {}
    for i in s:
        if i in hash_table: return False
        else: hash_table[i] = i
    return True

print(is_unique_with_dict('abcde'))
print(is_unique_with_dict('abcdee'))
print(is_unique_with_dict('aaaa'))
