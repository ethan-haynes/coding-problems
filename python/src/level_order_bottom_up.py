# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def level_order_bottom_up(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    lo_list = [[]]
    def traverse(root, depth=0):
        if root:
            if len(lo_list) - 1 < depth: lo_list.insert(0, [])
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
            lo_list[len(lo_list) - 1 - depth].append(root.val)

    traverse(root)
    return lo_list
                

