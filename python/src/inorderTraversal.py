def inorderTraversal(root):
    if root:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    return []
