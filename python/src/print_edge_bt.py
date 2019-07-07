class BinaryTree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_edge(root):
    if root:
        if root.left:
            print(f'{root.val}->{root.left.val}')
            print_edge(root.left)
        if root.right: 
            print(f'{root.val}->{root.right.val}')
            print_edge(root.right)
        if not root.left and not root.right:
            print(f'{root.val}')

bt = BinaryTree(8)
bt.left = BinaryTree(4)
bt.left.right = BinaryTree(6)
bt.left.left = BinaryTree(2)
bt.right = BinaryTree(16)
bt.right.right = BinaryTree(18)
bt.right.left = BinaryTree(12)

print_edge(bt)
