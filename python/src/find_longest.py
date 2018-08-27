def find_longest(words, chars):
    longest = ''

    for word in words:
        tmp_chars = chars.copy()
        if len(word) > len(longest):
            found_longest = True
            for letter in word:
                if letter in tmp_chars:
                    tmp_chars.remove(letter)
                else:
                    if '*' in tmp_chars:
                        tmp_chars.remove('*')
                    else:
                        found_longest = False
                        break
            if found_longest:
                longest = word
    
    return longest


print(find_longest(['cat', 'bird', 'coffee', 'apple', 'applez', 'ape'], ['*','a','b','p','p','l','e']))
