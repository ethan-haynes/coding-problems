def is_valid_bst(root):
    def getMin(root):
        if root:
            return min(root.val, getMin(root.left), getMin(root.right))
        return float('inf')

    def getMax(root):
        if root:
            return max(root.val, getMax(root.left), getMax(root.right))
        return -float('inf')

    if root:
        if getMax(root.left) < root.val < getMin(root.right):
            return isValid(root.left) and isValid(root.right)

        return False

    return True
