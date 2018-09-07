# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    out = [[]]
    def traverse(root, i):
        if root:
            if len(out) - 1 < i:
                out.append([root.val])
            else:
                out[i].append(root.val)
            traverse(root.left, i+1)
            traverse(root.right, i+1)
    traverse(root, 0)
    return out

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(level_order(t))
