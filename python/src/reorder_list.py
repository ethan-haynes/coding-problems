# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if head:
        node, nodes, from_back = head.next, [], True
            
        while(node):
            nodes.append(node)
            node = node.next
                
        node = head
            
        while(len(nodes)):
            if from_back: node.next = nodes.pop()
            else: node.next = nodes.pop(0)
            node, from_back = node.next, not from_back
            node.next = None
            

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

reorderList(head)

next = head
while(next):
    print(next.val)
    next = next.next
