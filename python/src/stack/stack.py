class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data):
        self.top = self.Node(data)

    def pop(self):
        data = None
        if self.top:
            data = self.top.data
            self.top = self.top.next
        return data

    def push(self, data):
        top = self.top
        self.top = self.Node(data)
        self.top.next = top

s = Stack(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
