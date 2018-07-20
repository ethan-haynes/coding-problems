def remove_nth_from(head, target):
    def __inner_remove(node):
        if not node.next: return None, 0
        _, num = __inner_remove(node.next)
        if num == target: node.next = node.next.next

        return node, num+1

    return __inner_remove(head)[0]

class LL:
    def __init__(self, val):
        self.val = val
        self.next = None

next = head = LL(0)
for i in range(1,5):
    next.next = LL(i)
    next = next.next


next = head
while next:
    print(next.val)
    next = next.next

head = remove_nth_from(head, 4)
print('---------------------')
next = head
while next:
    print(next.val)
    next = next.next
