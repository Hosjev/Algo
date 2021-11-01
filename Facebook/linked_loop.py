class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListLoop:

    def eval_start(self, node):
        # EC - empty or ONE
        if not node or not node.next:
            return
        head = pointer = offset = node
        while offset.next:
            pointer = pointer.next
            offset = offset.next.next
            if not offset: return
            if pointer == offset: break

        pointer = head
        while pointer != offset:
            pointer = pointer.next
            offset = offset.next
        return offset

def main():
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)
    ll.next.next.next.next.next = ll.next.next
    print(LinkedListLoop().eval_start(ll).value)


main()
