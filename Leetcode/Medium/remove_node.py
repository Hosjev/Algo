class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def remove_node(head, n):
    """ Remove nth node from tail """

    # Priming
    target_from_top = (count_nodes(head, 0) - n) + 1
    L = None
    P = head
    count = 0

    while P:
        count += 1
        if count == target_from_top:
            if not L:
                head = head.next
            else:
                L.next = P.next
            break
        else:
            L = P
            P = P.next


    return head


def count_nodes(node, count):
    if not node:
        return count
    else:
        return count_nodes(node.next, count + 1)


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
head.next.next.next.next = Node(5)

head = Node(0)
head.next = Node(1)

print(count_nodes(head, 0))
new_head = remove_node(head, 2)
cycle_nodes(new_head)
