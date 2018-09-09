# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# @param root, a tree link node
# @return nothing
def connect(root):
    next = [[]]
        
    def traverse(root, depth=0):
        if root:
            if len(next) - 1 < depth: next.append([]) 
            traverse(root.right, depth+1)
            traverse(root.left, depth+1)
            if len(next[depth]):
                root.next = next[depth].pop(0)  
            next[depth].append(root)
            
    traverse(root)
