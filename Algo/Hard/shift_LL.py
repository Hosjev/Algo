"""
Write a function that shifts a linked list by "k" moves. So a "2" would mean moving head to the right by 2. A 4, moving head by 4. Large numbers acceptable so handle with a modulus offset. Negative # acceptable so handle these with the remainder from modulus. * These calcs help you determine the new "tail", not head. (see below)

*** This could not be important. OBJECT COPIES ARE SHALLOW.

Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5
    k = 2

Output:
    4 -> 5 -> 0 -> 1 -> 2 -> 3

* calculating position of new tail:
      (length of 6) --determine wraparound offset, if any
                    --positions determined thus: p1, p2, p3, p4, p5, p6
                    --2 % 6 = 2 -- 6 - 2 = 4 <-position of new tail
                    --8 % 6 = 2 -- 6 - 2 = 4 <-position of new tail
                    --(-4) % 6 = 2 -- 6 - 2 = 4 <-position of new tail
                    --(-10) % 6 = 2 -- 6 - 2 = 4 <-position of new tail
                    --(6) % 6 = 0 if offset leads us to head, exit w/o changes

answer - O(1)
       - O(WS + NM)S
"""
import time


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle(node):
    if not node:
        return
    print(node.value)
    cycle(node.next)


def shiftedLinkedList(head, k):
    # Get length AND establish old tail
    length_of_object = 1
    old_tail = head # shallow
    while old_tail.next is not None:
        old_tail = old_tail.next
        length_of_object += 1

    # This hot mess is necessary to handle negative numbers and wraparounds
    offset = abs(k) % length_of_object # say where k is 6 and len is 6
    if offset == 0: return head
    # If positive #, we go forward, else go back (-8) % 6 = 4 (8) % 6 = 2
    new_tail_position = length_of_object - offset if k > 0 else offset
    new_tail = head # shallow
    while (new_tail_position - 1) != 0:
        new_tail = new_tail.next
        new_tail_position -= 1

    # Now we have our 2 pointers within the object
    pointer = new_tail.next # this is our new head
    new_tail.next = None # we make it official
    old_tail.next = head # the given pointer

    # Now we can return the new head with pointers corrected
    return pointer


def get_depth(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


if __name__ == "__main__":


    # In this example, p2 travels 12 steps around, p1 6: 12-6 = 6/2 = 3 (distance from their meeting point to remaining loop, or the start of the loop)
    ll = LinkedList(0)
    l1 = LinkedList(1)
    #ll.next = LinkedList(1)
    l2 = LinkedList(2)
    l3 = LinkedList(3)
    l4 = LinkedList(4)
    l5 = LinkedList(5)
    ll.next = l1
    ll.next.next = l2
    ll.next.next.next = l3
    ll.next.next.next.next = l4
    ll.next.next.next.next.next = l5

    l = shiftedLinkedList(ll, 2)
    cycle(l)
