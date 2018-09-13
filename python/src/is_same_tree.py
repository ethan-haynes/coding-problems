def is_same_tree(t1, t1):
    if not t1 and not t1: return True
    if t1 or t1: return False
    if t1.val == t2.val:
        return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)
    return False
