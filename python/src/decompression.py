# in : 3[abc]4[ab]c
# out: abcabcabcababababc
def decomp(s):
    open, close = s.find('['), s.find(']')
    if open == -1 and close == -1: return s
    if open == -1 and close > -1 or close < open:
        return s[:close]

    sub = s[open+1:]
    total = int(''.join([ val for val in s[:open] if val.isdigit()]))
    return total*decomp(sub) + decomp(s[close+1:])

print(decomp('3[3[abc]]4[ab]c'))

#
# def decomp(s):
#     open, close = s.find('['), s.find(']')
#     if open == -1: return s
#
#     sub = s[open+1:close]
#     total = int(''.join([ val for val in s[:open] if val.isdigit()]))
#     return total*decomp(sub) + decomp(s[close+1:])
#
# print(decomp('3[abc]4[ab]c'))
