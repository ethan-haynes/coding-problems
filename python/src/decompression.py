# in : 3[abc]4[ab]c
# out: abcabcabcababababc
def decomp(s):
    FIND_NUM, FIND_CLOSE   = 'FIND_NUM', 'FIND_CLOSE'
    open, close = -1, -1
    total = ''

    state = FIND_NUM
    stack = []
    for i, val in enumerate(s):
        if state == FIND_NUM:
            if val.isdigit(): total += val
            elif len(total) == 0: continue
            else:
                state, open = FIND_CLOSE, i
                stack.append(i)
                total = int(total)
        elif state == FIND_CLOSE:
            if val == '[':
                stack.append(i)
            elif val == ']':
                stack.pop()
                if len(stack) == 0:
                    close = i
                    break

    if open == close and open == -1: return s

    return total*decomp(s[open+1:close]) + decomp(s[close+1:])

print(decomp('3[3[abc]]4[gg]c'))
