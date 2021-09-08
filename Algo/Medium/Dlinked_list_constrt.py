"""
Write a DoublyLinkedList class that has a head and tail, both of which point to either
a linked list Node or None.
    -setting head and tail of linked list
    -inserting nodes before and after other nodes as well as at given positions
     (head node position is 1)
    -removing given nodes and removing nodes with given values
    -searching for nodes with given values

Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition and remove
methods all take in actual Node(s) as input (objects not values). Except insertAtPosition
which takes obj and an int representing the position. --this means you don't need to create
new nodes inside these methods. The input nodes can be either stand-alone nodes or nodes that
are already in the LL. If they're already LL nodes, the methods will effectively be
'moving' the nodes within the LL. You won't be told if the input nodes are already in the
LL, so your code will have to defensively handle this scenario.

Each node has a prev and next node and a value integer.

* Assume this linked list has been created.
1 <-> 2 <-> 3 <-> 4 <-> 5

* Assume we have these standalone nodes:
3, 3, 6

setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5
setTail(6): ...5 <-> 6
insertBefore(6, 3): ...5 <-> 3 <-> 6
insertAfter(6, 3): ...3 <-> 6 <-> 3
insertAtPosition(1, 3): 3 <-> 4 <-> 1...
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6
remove(2): 4 <-> 1 <-> 5 <-> 6
containsNodeWithValue(5): True

Output:
    MinHeap(array) - instantiating calls method below
    buildHeap(array): [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
    insert(76) (end)
    peak(): -5
    remove(): -5
    peak(): 2
    remove(): 2
    peak(): 6
    insert(87) (end)

O(n)T | O(1)S
"""
import time

def wcycle(node):
    # Straight code loop
    while True:
        time.sleep(.3)
        print(node.value, end=" : ")
        print(node.prev.value, end=" : ") if node.prev else print("None", end=" : ")
        print(node.next.value) if node.next else print("None")
        if node.next:
            node = node.next
        else:
            break


def cycle(node):
    # Recursive
    time.sleep(.3)
    print(node.value, end=" : ")
    print(node.prev.value, end=" : ") if node.prev else print("None", end=" : ")
    print(node.next.value) if node.next else print("None")
    if node.next:
        cycle(node.next)
    else:
        return


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # Of the methods below: inserts and remove take in singleton or simply
        # move around added Nodes to LL

    def setHead(self, node):
        # Write your code here.
        # O(1)T -- O(1)S
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        # O(1)T -- O(1)S
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        # O(1)T -- O(1)S
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        # O(1)T -- O(1)S
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        # O(p)T -- O(1)S
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        idx = 1
        # Below we merely use while to increment until reaching the index position
        while node and idx != position:
            node = node.next
            idx += 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        # O(n)T -- O(1)S
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # Write your code here.
        # O(1)T -- O(1)S
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.update_pointers(node)

    def update_pointers(self, node):
        # Update outbound pointers 1st
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # To be nullified
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        # O(n)T -- O(1)S
        node = self.head
        while node:
            if node.value == value:
                return True
            else:
                node = node.next
        return False



if __name__ == "__main__":


    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(5)
    head.next.next.next.next.prev = head.next.next.next

    wcycle(head)

    d = DoublyLinkedList()
    d.setHead(head)
    print(d.containsNodeWithValue(1))
    print(d.containsNodeWithValue(5))
    print(d.containsNodeWithValue(7))
    print(d.tail.value)
    d.remove(head.next)
    print("Deleted:")
    wcycle(head)

    # Inserts
    head.next.next.next.next = Node(8)
    head.next.next.next.next.prev = head.next.next.next
    d.setTail(head.next.next.next.next)
    print("Inserted 8:")
    wcycle(head)
    # Inserting singleton node works
    # d.insertBefore(head.next, Node(8))
    d.insertBefore(head.next, head.next.next.next.next)
    print("Moved 8:")
    wcycle(head)
    # Now head.next is 8 then 3
    print("Moved ?:")
    d.insertAfter(head.next, head.next.next.next)
    wcycle(head)
    # Now shit is fucked up. Slaughter it.
    print("Moved 10:")
    d.insertAtPosition(2, Node(10))
    wcycle(head)
    # Shit is SO fucked. Slaughter it.
    print("Removed val 4")
    d.removeNodesWithValue(4)
    wcycle(head)
