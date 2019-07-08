class BinaryTree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_sum(root, total=0):
    if root == None:
        return 0
    
    total += root.val

    if root.left and root.right:
        left, right =  max_sum(root.left), max_sum(root.right)
        return max(
            left, right,
            max_sum(root.left, total), max_sum(root.right, total), total
        )
    elif root.left:
        left = max_sum(root.left)
        return max(total, left, max_sum(root.left, total))
    elif root.right:
        right = max_sum(root.right)
        return max(right, left, max_sum(root.right, total))
    else:
        return root.val

root = BinaryTree(8)
root.left = BinaryTree(4)
root.left.right = BinaryTree(6)
root.left.left = BinaryTree(2)
root.right = BinaryTree(-16)
root.right.right = BinaryTree(32)
root.right.left = BinaryTree(10)

print(max_sum(root))


root = BinaryTree(-8)
root.left = BinaryTree(-4)
root.left.right = BinaryTree(-6)
root.left.left = BinaryTree(2)
root.right = BinaryTree(-16)
root.right.right = BinaryTree(-32)
root.right.left = BinaryTree(-10)

print(max_sum(root))
