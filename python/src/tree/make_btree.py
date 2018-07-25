import math
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# make binary search tree from sorted array
def make_btree(arr):
    if not len(arr): return None
    mid = math.floor(len(arr)/2)
    head = Tree(arr[mid])
    head.left, head.right = make_btree(arr[:mid]), make_btree(arr[mid+1:])
    return head

def traverse(root):
    if root:
        traverse(root.left)
        print(root.data)
        traverse(root.right)

t = make_btree([1,2,3,4,5,6,7,8,9])
traverse(t)
