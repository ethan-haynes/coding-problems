def is_sym1(root):
    def __sym__(r1, r2):
        sym = True
        if r1 and r2:
            if r1.val != r2.val:
                sym = False
            else:
                sym = __sym__(r1.left, r2.right) and __sym__(r1.right, r2.left)
        elif r1 or r2: 
            sym = False

        return sym

    return __sym__(root.left, root.right)
    
def is_sym2(root):
    q = []
    q.append(root), q.append(root)
    while q:
        r1, r2 = q.pop(), q.pop()
        if not r1 and not r2:
            continue
        if r1 or r2:
            return False
        if r1.val != r2.val:
            return False
        q.append(r1.left), q.append(r2.right)
        q.append(r1.right), q.append(r2.left)

    return True

