class Stack:
    """
        Outter Stack class with logic to keep track of min value
        Contains inner stack to manage min values
        O(1) for push, pop, and min methods
    """
    class Node:
        """ Inner node class """
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data=None):
        self._min = self.first = None
        if data != None:
            self.first = self.Node(data)
            self._min = self.Node(data)

    def push(self, data):
        if self.first:
            first = self.first
            self.first = self.Node(data)
            self.first.next = first
            if data < self.min():
                _min = self._min
                self._min = self.Node(data)
                self._min.next = _min
        else:
            self.first = self.Node(data)
            self._min = self.Node(data)

    def pop(self):
        if self.first:
            data = self.first.data
            self.first = self.first.next
            if data == self.min(): self._min = self._min.next
            return data

    def min(self):
        if self._min:
            return self._min.data


s = Stack(0)
s.push(1)
s.push(2)
s.push(3)
s.push(-1)
print(s.min())
print(s.pop())
print(s.min())
