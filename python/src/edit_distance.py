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

def ed(str1, str2, memo=None):
    if str1 == str2:
        return 0
    
    n = len(str2)
    if memo == None:
        memo = dict()

    if str1 not in memo:
        for i,ch1 in enumerate(str1):
            if i == n:
                memo[str1] = 1 + ed( str1[:i] + str1[i+1:], str2, memo)
                return memo[str1]
            ch2 = str2[i]
            if ch1 != ch2:
                memo[str1] = 1 + min(
                        ed(str1[:i] + str1[i+1:], str2, memo),
                        ed(str1[:i] + ch2 + str1[i+1:], str2, memo),
                        ed(str1[:i] + ch2 + str1[i:], str2, memo))
                return memo[str1]
            memo[str1] = float("inf")
         
    return memo[str1]

print(edit_distance("Anshuman", "Antihuman"))
print(ed("Anshuman", "Antihuman"))
