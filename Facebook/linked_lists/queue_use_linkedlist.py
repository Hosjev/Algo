class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class FifoQueue:

    def __init__(self):
        self.head = Node("head")
        self.tail = None
        self.head.next = self.tail

    def enqueue(self, item):
        node = Node(item)
        if not self.tail:
            self.head.next = node
        else:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        node = self.head.next
        if not node: return None
        next = node.next
        self.head.next = next
        return node.value


def main():
    q = FifoQueue()
    print(q.dequeue())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    q.enqueue(5)
    print(q.dequeue())


main()
