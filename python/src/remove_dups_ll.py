class LL(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_dups_ll(head):
    def remove(node, val=''):
        if not node.next: return -1
        if node.next.val == val:
            node.next = node.next.next
            return val
        else:
            return remove(node.next, val)

    node = head
    while node:
        while remove(node, node.val) == node.val: pass
        node = node.next

head = LL(0)
next = head
for i in range(1,21):
    next.next = LL(i%10)
    next = next.next

next = head
while next:
    print(next.val)
    next = next.next
print("========================")
remove_dups_ll(head)

next = head
while next:
    print(next.val)
    next = next.next
