"""
Write a function that takes in the head of a Singly Linked List, reverses the list in place (don't create new list), and returns its new head.

Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5

Output:
    5 -> 4 -> 3 -> 2 -> 1 -> 0

answer - O(1)
       - O(WS + NM)S
"""
import time


class Node:
    def __init__(self, value):
        self.value = value


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # get moves; janky and horrible
    tail = None
    current = head # shallow

    while current is not None:
        future = current.next
        current.next = tail
        tail = current
        current = future

    return tail


def cycle(node):
    if node is None:
        return
    print(node.value)
    cycle(node.next)



if __name__ == "__main__":


    # In this example, p2 travels 12 steps around, p1 6: 12-6 = 6/2 = 3 (distance from their meeting point to remaining loop, or the start of the loop)
    LL = LinkedList(0)
    LL.next = LinkedList(1)
    LL.next.next = LinkedList(2)
    LL.next.next.next = LinkedList(3)
    LL.next.next.next.next = LinkedList(4)
    LL.next.next.next.next.next = LinkedList(5)
    cycle(LL)

    r = reverseLinkedList(LL)
    cycle(r)
