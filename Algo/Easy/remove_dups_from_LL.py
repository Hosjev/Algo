"""
Given head of singly-linked list whose nodes are in order. Write function that returns same object with no DUPS.
Alter in place.

Input:
    ll = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
Output:
    1 -> 3 -> 4 -> 5 -> 6

"""
import time


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_pretty(node):
    print(node.value)
    if node.next is None:
        return
    else:
        print_pretty(node.next)


def removeDuplicatesFromLinkedList(node):
    # Write your code here.

    def _inner_recur(node):
        if node:
            # look forward 5, 6, 6
            print(node.value)
            if node.next:
                while (node.value == node.next.value):
                    node.next = node.next.next
                    if node.next is None:
                        break
            return _inner_recur(node.next)
        else:
            return

    return _inner_recur(node)


# write node object
head = LinkedList(1)
head.next = LinkedList(1)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(4)
head.next.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next.next = LinkedList(6)
head.next.next.next.next.next.next.next.next = LinkedList(6)

head = LinkedList(1)
head.next = LinkedList(9)
head.next.next = LinkedList(11)
head.next.next.next = LinkedList(15)
head.next.next.next.next = LinkedList(15)
head.next.next.next.next.next = LinkedList(16)
head.next.next.next.next.next.next = LinkedList(17)


# print_pretty(head)
removeDuplicatesFromLinkedList(head)
print_pretty(head)
