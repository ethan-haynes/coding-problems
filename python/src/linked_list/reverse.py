class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(root):
    dummy_head = Node(0)
    def __rev__(root):
        if root:
            node = __rev__(root.next)
            node.next = root
            node.next.next = None
            return node.next
        else:
            return dummy_head
    __rev__(root)
    return dummy_head.next

def reverse2(root):
    if not root: return root
    def __rev__(root):
        node = head = None
        if root:
            node, head = __rev__(root.next)
            root.next = None
            if not head:
                node = head = root
            else:
                node.next = root
                node = node.next
        return node, head
    _, head = __rev__(root)
    return head
    

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next = Node(3)

next = head
while next:
    print(next.val)
    next = next.next

next = reverse(head)
while next:
    print(next.val)
    next = next.next

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next = Node(3)

next = reverse2(head)
while next:
    print(next.val)
    next = next.next
