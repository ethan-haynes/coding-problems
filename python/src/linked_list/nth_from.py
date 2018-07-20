def remove_nth_from(head, target):
    def __inner_remove(node, count=0):
        if not node.next: return None, 0, count
        _, num, total = __inner_remove(node.next, count+1)

        if num == target: node.next = node.next.next # case for all except head
        elif num+1 == total: node = node.next # case for head of LL

        return node, num+1, total

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
