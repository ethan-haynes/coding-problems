"""
    Queue implemented with 2 stacks
"""
class MyQueue:
    class Stack:
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        def __init__(self, data=None):
            self.first = None
            if data != None:
                self.first = self.Node(data)

        def push(self, data):
            if self.first:
                first = self.first
                self.first = self.Node(data)
                self.first.next = first
            else:
                self.first = self.Node(data)

        def pop(self):
            if self.first:
                first = self.first
                self.first = self.first.next
                return first.data

        def peek(self):
            if self.first: return self.first.data

    def __init__(self, data):
        self.s1 = self.Stack(data)
        self.s2 = self.Stack()

    def enqueue(self, data):
        if self.s1.peek() != None:
            while(self.s1.peek() != None):
                self.s2.push(self.s1.pop())
            self.s1.push(data)
            while(self.s2.peek() != None):
                self.s1.push(self.s2.pop())

    def dequeue(self):
        if self.s1.peek() != None: return self.s1.pop()

q = MyQueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
