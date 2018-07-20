"""
    TASK: find the node that is referenced twice in a circular linked list
    NOTE: Recursive Solution
"""
def find_loop_start(head):
    hash = {}
    def __find_loop_inner(node):
        if not node: return None
        _id = id(node)
        if _id in hash: return node
        else:
            hash[_id] = 1
            return __find_loop_inner(node.next)
    return __find_loop_inner(head)

"""
    TASK: find the node that is referenced twice in a circular linked list
    NOTE: Iterative Solution
"""
def find_loop_start_itr(head):
    hash, node = {}, head
    while node:
        _id = id(node)
        if _id in hash: return node
        else:
            hash[_id] = 1
            node = node.next


class LL:
    def __init__(self, val):
        self.val = val
        self.next = None

h = LL(0)
h.next = LL(1)
h.next.next = h

node = find_loop_start(h)
print(node.val if node else node)
node = find_loop_start_itr(h)
print(node.val if node else node)
