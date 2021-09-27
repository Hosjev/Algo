class SLL:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_LL_nums(node1, node2):
    """
    1. node helper returns concatenated strings
    2. we sum them on the return
    3. we finally return the next helper to build SLL
       a. they want this in REVERSE (1st digit = tail)
    """
    ll_sum = int(node_helper(node1)) + int(node_helper(node2))
    return linked_list_maker(str(ll_sum), len(str(ll_sum)) - 1)


def node_helper(node):
    if not node:
        return 0
    else:
        accumulated_integers = node_helper(node.next)

    # Return these concatenations up the stack
    return str(accumulated_integers) + str(node.val)


def linked_list_maker(digits, digit_position):
    if digit_position < 0:
        return None
    else:
        node = SLL(digits[digit_position])
        node.next = linked_list_maker(digits, digit_position - 1)
    return node


def cycle(node):
    if not node:
        return
    else:
        print(node.val)
        return cycle(node.next)



head1 = SLL(2)
head1.next = SLL(4)
head1.next.next = SLL(3)

head2 = SLL(5)
head2.next = SLL(6)
head2.next.next = SLL(4)

print(add_two_LL_nums(head1, head2))
head = add_two_LL_nums(head1, head2)
print(cycle(head))
