def length_of_last_word(s=''):
    """
        :type s: str
        :rtype: int
    """
    return len(s.split()[-1])

print(length_of_last_word('hello world'))
print(length_of_last_word('hello'))
print(length_of_last_word('hi hello how are you'))
