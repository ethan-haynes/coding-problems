class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data=None):
        self.last = self.first = None
        if data:
            self.last = self.first = self.Node(data)

    def enqueue(self, data):
        if not self.first:
            self.last = self.first = self.Node(data)
        else:
            self.last.next = self.Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.first:
            data = self.first.data
            self.first = self.first.next
            return data

q = Queue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
q = Queue()
print(q.dequeue())
q.enqueue(100)
print(q.dequeue())
