class SetStack:
    class Stack:
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        def __init__(self, data=None):
            self.first, self.size = None, 0
            if data != None:
                self.first = self.Node(data)
                self.size += 1

        def push(self, data):
            if self.first:
                first = self.first
                self.first = self.Node(data)
                self.first.next = first
            else:
                self.first = self.Node(data)
            self.size += 1

        def pop(self):
            if self.first:
                self.size -= 1
                data = self.first.data
                self.first = self.first.next
                return data

    def __init__(self, data=None):
        self.threshold, self.set = 3, []
        if data != None:
            node = self.Stack(data)
            self.set.append(node)

    def push(self, data):
        if len(self.set) != 0:
            node = self.set[-1]
            if node == None or node.size == self.threshold:
                node = self.Stack(data)
                self.set.append(node)
            else:
                node.push(data)
        else: self.set.append(self.Stack(data))

    def pop(self):
        if len(self.set) != 0:
            node = self.set[-1]
            data = node.pop()
            if node.size == 0: self.set = self.set[:-1]
            return data


s = SetStack()
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
