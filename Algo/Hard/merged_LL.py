"""
Write a function that takes in the heads of 2 Singly Linked Lists that are in sorted order, respectively. Merge the lists in place (shouldn't create a brand new list) and return the head of the merged lists; the merged list should be in sorted order.

You can assume that the input LL will always have at least one node. Head will never be None.
*** This could not be important. OBJECT COPIES ARE SHALLOW.

Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5

Output:
    5 -> 4 -> 3 -> 2 -> 1 -> 0

answer - O(1)
       - O(WS + NM)S
"""
import time


class Node:
    def __init__(self, id):
        self.id = id


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle(node):
    if not node:
        return
    print(node)
    cycle(node.next)


def mergeLinkedLists(headOne, headTwo):
    # Tracking 3 variables
    # obj = the main obj passed (grows smaller)
    # obj2 = the remaining nodes (the temp var)
    # backward = my growing answer
    p1 = headOne # Shallow copy
    p1_object = None
    p2 = headTwo # Shallow copy
    
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            print(f"Condition met ({p1.value} less than {p2.value})")
            p1_object = p1
            p1 = p1.next
        else:
            # Greater than or equal-to
            if p1_object is not None: # Not head
                p1_object.next = p2
            p1_object = p2
            p2 = p2.next
            p1_object.next = p1

    if p1 is None:
        p1_object.next = p2
    return headOne if headOne.value < headTwo.value else headTwo


if __name__ == "__main__":


    # In this example, p2 travels 12 steps around, p1 6: 12-6 = 6/2 = 3 (distance from their meeting point to remaining loop, or the start of the loop)
    ll = LinkedList(1)
    l2 = LinkedList(3)
    l3 = LinkedList(5)
    ll.next = l2
    ll.next.next = l3

    ll2 = LinkedList(0)
    l22 = LinkedList(2)
    l23 = LinkedList(4)
    ll2.next = l22
    ll2.next.next = l23

    ll = LinkedList(0)
    ll.next = LinkedList(2)
    ll2 = LinkedList(1)
    ll2.next = LinkedList(3)

    l = mergeLinkedLists(ll, ll2)
