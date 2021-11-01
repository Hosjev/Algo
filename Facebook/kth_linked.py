class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListKthEnd:

    def total_nodes(self, node, t):
        if not node:
            return t
        return self.total_nodes(node.next, t + 1)

    def eval(self, node, k):
        # Edge Case(s)
        if not node: return
        total = self.total_nodes(node, 0)
        if total > k: return

        count = 1
        while (total - k) != count:
            node = node.next
            count += 1
        return node


def main():
    tree = Node(1)
    tree.next = Node(2)
    tree.next.next = Node(3)
    tree.next.next.next = Node(4)
    tree.next.next.next.next = Node(5)
    tree.next.next.next.next.next = Node(6)
    tree.next.next.next.next.next.next = Node(7)
    tree.next.next.next.next.next.next.next = Node(8)
    tree.next.next.next.next.next.next.next.next = Node(9)
    print(LinkedListKthEnd().eval(tree, 3).value)


main()
