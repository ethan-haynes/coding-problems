# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def kthSmallest(root, k, counter=None):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if counter == None: counter = {'count':1}
    if root:
        val = kthSmallest(root.left, k, counter)
            
        if val != None: return val
        if len(counter) == k: return root.val
        
        counter.count += 1
        kthSmallest(root.right, k, counter)
            
    return k
