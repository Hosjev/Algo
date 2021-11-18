class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListKthEnd:
    """ O(N) twice """
    def total_nodes(self, node, t):
        if not node:
            return t
        return self.total_nodes(node.next, t + 1)

    def eval(self, node, k):
        # Edge Case(s)
        if not node: return
        total = self.total_nodes(node, 0)
        if k > total: return

        count = 1
        while (total - k) != count:
            node = node.next
            count += 1
        return node


def main():
    linkedlist = Node(1)
    linkedlist.next = Node(2)
    linkedlist.next.next = Node(3)
    linkedlist.next.next.next = Node(4)
    linkedlist.next.next.next.next = Node(5)
    linkedlist.next.next.next.next.next = Node(6)
    linkedlist.next.next.next.next.next.next = Node(7)
    linkedlist.next.next.next.next.next.next.next = Node(8)
    linkedlist.next.next.next.next.next.next.next.next = Node(9)
    print(LinkedListKthEnd().eval(linkedlist, 3).value)


main()
