def eval_rpn(tokens):
    if tokens and len(tokens):
        stack = []
        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                n2, n = stack.pop(), stack.pop()
                if t == '*':
                    n *= n2
                elif t == '/':
                    n = int(float(n)/n2)
                elif t == '-':
                    n -= n2
                else:
                    n += n2
                stack.append(n)

    return stack.pop()

