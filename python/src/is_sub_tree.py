class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_sub_tree(r1, r2):

    def is_sub(r1, r2):
        if not r1 and not r2:
            return True
        if r1 and not r2:
            return True
        if not r1 and r2:
            return False

        if r1.val == r2.val:
            return is_sub(r1.left, r2.left) and is_sub(r1.right, r2.right)
        else: return False

    def bfs(r1, r2):
        if r1:
            return is_sub(r1, r2) or bfs(r1.left, r2) or bfs(r1.right, r2)
        else: return False

    return bfs(r1, r2)

head = Tree(3)
head.left = Tree(1)
head.left.left = Tree(0)
head.left.right = Tree(2)
head.right = Tree(5)
head.right.right = Tree(6)
head.right.left = Tree(4)

head2 = Tree(5)
head2.right = head.right

print(is_sub_tree(head, head))
print(is_sub_tree(head, head.left))
print(is_sub_tree(head, head.right))
print(is_sub_tree(head, head2))
