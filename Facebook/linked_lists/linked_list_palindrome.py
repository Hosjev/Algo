class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListPalindrome:

    def cycle(self, node, arr):
        if not node:
            return
        arr.append(node.value)
        self.cycle(node.next, arr)
        return arr

    def cycle_make_obj(self, node):
        # Use LLP with (LL) inheritance of "insert" method
        # self.rev.insert(node.value)
        # below, move 2 pointers for fed obj and rev obj
        return

    def is_palindrome(self, head):
        arr = self.cycle(head, [])
        return arr == [x for x in reversed(arr)]


def main():
    head = Node("a")
    head.next = Node("b")
    head.next.next = Node("b")
    head.next.next.next = Node("b")
    print(LinkedListPalindrome().is_palindrome(head))


main()
