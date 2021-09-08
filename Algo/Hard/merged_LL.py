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


class LL:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle(node):
    if not node:
        return
    else:
        print(node.value)
        cycle(node.next)


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne # pointer
    p1_object = None
    p2 = headTwo # pointer
    
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

    head1 = LL(2)
    head1.next = LL(4)
    head1.next.next = LL(5)

    head2 = LL(1)
    head2.next = LL(2)
    head2.next.next = LL(3)

    new_head = (mergeLinkedLists(head1, head2))
    print(cycle(new_head))

