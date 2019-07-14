def edit_distance(str1, str2):
    if str1 == str2:
        return 0
    
    n = len(str2)
    
    for i,ch1 in enumerate(str1):
        if i == n:
            return 1 + edit_distance( str1[:i] + str1[i+1:], str2)
        ch2 = str2[i]
        if ch1 != ch2:
            return 1 + min(
                    edit_distance(str1[:i] + str1[i+1:], str2),
                    edit_distance(str1[:i] + ch2 + str1[i+1:], str2),
                    edit_distance(str1[:i] + ch2 + str1[i:], str2))
    
    return float("inf")

print(edit_distance("Anshuman", "Antihuman"))
