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


def main():
    s = Stack()
    [s.push(i) for i in range(5)]
    print(s.peek())
    s.push(5)
    s.pop()
    s.pop()
    print(s.peek())
    print(s.is_empty())

main()
