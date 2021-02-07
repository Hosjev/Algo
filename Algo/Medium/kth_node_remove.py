"""

1 <-> 2 <-> 3 <-> 4 <-> 5

Output: (none)


O(n)T | O(1)S
"""
import time

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_index_forward(node, k):
    count = 0
    while True:
        if not node:
            # We reached the end
            return count - k
        count += 1
        node = node.next


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    forward_idx = get_index_forward(head, k)
    if forward_idx < 0:
        return False
    elif forward_idx == 0:
        head.value = head.next.value
        head.next = head.next.next
    else:
        count = 1
        while count != forward_idx:
            head = head.next
            count += 1
        head.next = head.next.next

def removeKthNodeFromEndd(head, k):
    count = 1
    first = head
    second = head
    # Get intermediate index from k
    while count <= k:
        second = second.next
        count += 1
    # If our kth to remove is index 0
    if not second:
        head.value = head.next.value
        head.next = head.next.next
        return
    # Else, iterate until reaching intermediate
    while second.next:
        second = second.next
        first = first.next
    # We finally have the correct location of kth,
    # now we replace it with the Next object
    first.next = first.next.next


def cycle(node):
    # Straight code loop
    while node:
        time.sleep(.3)
        print(node.value)
        node = node.next


if __name__ == "__main__":


    singly_ll = LinkedList(0)
    singly_ll.next = LinkedList(1)
    singly_ll.next.next = LinkedList(2)
    singly_ll.next.next.next = LinkedList(3)
    singly_ll.next.next.next.next = LinkedList(4)
    singly_ll.next.next.next.next.next = LinkedList(5)
    singly_ll.next.next.next.next.next.next = LinkedList(6)
    singly_ll.next.next.next.next.next.next.next = LinkedList(7)
    singly_ll.next.next.next.next.next.next.next.next = LinkedList(8)
    singly_ll.next.next.next.next.next.next.next.next.next = LinkedList(9)

    #cycle(singly_ll)

    removeKthNodeFromEnd(singly_ll, 10)

    cycle(singly_ll)
