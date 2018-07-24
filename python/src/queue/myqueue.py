"""
    Queue implemented with 2 stacks
"""
class MyQueue:
    def __init__(self, data):
        self.s1 = [data]
        self.s2 = []

    def enqueue(self, data):
        if len(self.s1):
            while(len(self.s1)):
                self.s2.append(self.s1.pop())
            self.s1.append(data)
            while(len(self.s2)):
                self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1): return self.s1.pop()

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
