"""
Write a function that takes in the head of a Singly Linked List that contains a loop (the list's tail node points to some node in the list instead of None). The function should the node (the actual node not just its value) from which the loop originates in constant space.

Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                               ^         v
                               9 <- 8 <- 7
Output:
    4 -> 5 -> 6
    ^         v
    9 <- 8 <- 7

* pointer 1 steps 1
* pointer 2 steps 2
* when p1 == p2, stop--(p2*2) -(p1) / 2 == remaining steps to start of loop
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


def findLoop(head):
    # 1-set 2 pointers to travel the entirety of the list (until meeting at 1st pointer)
    # 2-1st pointer gets reset to head and travels the distance to meet 2nd again
    # This rhythm is predicated on the loop existing at tail
    pointer_one = head.next # position 1
    pointer_two = head.next.next # position 2
    # Zero node non-inclusive here
    while pointer_one != pointer_two:
        # Also, we're observing objects, not values
        pointer_one = pointer_one.next # advance 1
        pointer_two = pointer_two.next.next # advance 2
    # Reset p1 to head
    pointer_one = head
    while pointer_one != pointer_two:
        pointer_one = pointer_one.next
        pointer_two = pointer_two.next
    return pointer_one # the START of the pointer contains all objects in loop


if __name__ == "__main__":


    # In this example, p2 travels 12 steps around, p1 6: 12-6 = 6/2 = 3 (distance from their meeting point to remaining loop, or the start of the loop)
    LL = LinkedList(Node(0))
    LL.next = Node(1)
    LL.next.next = Node(2)
    LL.next.next.next = Node(3)
    LL.next.next.next.next = Node(4)
    LL.next.next.next.next.next = Node(5)
    LL.next.next.next.next.next.next = Node(6)
    LL.next.next.next.next.next.next.next = Node(7)
    LL.next.next.next.next.next.next.next.next = Node(8)
    LL.next.next.next.next.next.next.next.next.next = Node(9)
    LL.next.next.next.next.next.next.next.next.next.next = LL.next.next.next.next #4

    print(findLoop(LL))

