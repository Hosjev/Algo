class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def swap_nodes(head):
    """ Swap nodes every adjacent node (2)"""

    # Priming
    L = None
    two_prior = None
    P = head
    count = 0

    while P:
        count += 1
        if count == 2:
            if two_prior:
                two_prior.next = P
            L.next = P.next
            P.next = L
            # Handle head
            if not two_prior:
                head = P
            P = L.next
            count = 0
            two_prior = L
        else:
            L = P
            P = P.next

    return head


def cycle_nodes(node):
    if not node:
        return None
    else:
        print(f"...cycle: {node.val}")
        return (cycle_nodes(node.next))



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

nh = swap_nodes(head)
print(cycle_nodes(nh))
