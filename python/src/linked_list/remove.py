class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.next = None
        self.prev = prev

def remove1(head, target):
    d_head = Node(0)
    d_head.next, head.prev = head, d_head

    def __rem(root):
        if root:
            if root.val == target:
                if root.next:
                    root.prev.next, root.next.prev = root.next, root.prev
                else:
                    root.prev.next = None
            else:
                __rem(root.next)

    __rem(head)

    if d_head.next: d_head.next.prev = None

    return d_head.next

head = Node(0)
head.next = Node(1, head)
head.next.next = Node(2, head.next)
head.next.next.next = Node(3, head.next.next)

remove1(head, 2)
next = head
while next:
    print(next.val)
    next = next.next
