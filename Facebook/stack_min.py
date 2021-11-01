class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.head.next = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        return data

    def pop(self):
        if self.is_empty(): return
        node = self.head.next
        self.head.next = node.next
        self.size -= 1
        return node.value

    def peek(self):
        if self.is_empty(): return
        return self.head.next.value

    def is_empty(self):
        return self.size == 0

class StackMinimum(Stack):

    def __init__(self):
        # Super inst delegation of self
        super().__init__()
        self.top = None
        # Locally instantiated object
        self.mins = Stack()

    def minimum(self):
        if not self.top: return float("inf")
        else: return self.mins.peek()

    def push(self, data):
        super().push(data)
        if data < self.minimum():
            self.mins.push(data)
            self.top = data

    def pop(self):
        data = super().pop()
        if data == self.minimum():
            self.mins.pop()
        return data


def main():
    # StackMin is abstracted
    sm = StackMinimum()
    sm.push(3)
    sm.push(2)
    sm.push(1)
    sm.push(2)
    print(sm.head.next.value)
    print(sm.minimum())

main()
