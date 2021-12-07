class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def hasCycle(self, head) -> bool:
        by_one = head
        by_two = head

        while True:
            try:
                by_one = by_one.next
                by_two = by_two.next.next
                if by_one.val == by_two.val:
                    return True
            except AttributeError:
                return False


if __name__ == "__main__":
    h = Node(1)
    h.next = Node(2)
    h.next.next = Node(3)
    h.next.next.next = Node(4)
    h.next.next.next = h.next
    print(Solution().hasCycle(h))
