def scoreOfParentheses(S: str) -> int:
    size = len(S)
    stack = score = i = 0

    while i < size:
        if S[i] == '(':
            stack += 1
        else:
            stack -= 1
            score += 2**stack
            while i+1 < size and s[i+1] == ')':
                stack -= 1
                i += 1
        i += 1

    return score

