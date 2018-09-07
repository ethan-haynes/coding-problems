# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        l_d = 1 + maxDepth(root.left)
        r_d = 1 + maxDepth(root.right)
        depth = l_d if r_d < l_d else r_d
    else:
        depth = 0
    return depth

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(level_order(t))
