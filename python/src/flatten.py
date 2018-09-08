def flatten(root):
    head = None

    def traverse(root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            traverse(root.right)
            traverse(root.left)
            root.right = head
            root.left = None
            head = root

    traverse(root)
