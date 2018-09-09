class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def has_cycles(root, memo=None):
    if memo == None: memo = set()
    if root:
        node_id = id(root)
        if node_id not in memo:
            memo.add(node_id)
            return has_cycles(root.next, memo)
        else: return True
    else: return False

head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = head 

print(has_cycles(head))

head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)

print(has_cycles(head))
