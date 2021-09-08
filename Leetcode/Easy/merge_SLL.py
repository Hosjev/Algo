class LL:
    def __init__(self, value):
       self.value = value
       self.next = None


def cycle(head):
    if not head:
        return
    else:
        print(head.value)
        cycle(head.next
)

def merge_singly_linked_lists(head1, head2):
    """
    1. start with pointer
    2. declare head pointers
    3. move the pointers along
    4. return winning head
    """
    H1 = head1
    H2 = head2
    pointer = None

    while H1 and H2:
        if H1.value < H2.value:
            pointer = H1
            H1 = H1.next
        else:
            if pointer:
                pointer.next = H2
            pointer = H2
            H2 = H2.next
            pointer.next = H1

    # This horrible magic to maintain the pointers
    if not H1:
        pointer.next = H2

    return head1 if head1.value < head2.value else head2


head1 = LL(1)
head1.next = LL(2)
head1.next.next = LL(4)

head2 = LL(1)
head2.next = LL(3)
head2.next.next = LL(4)

new_head = merge_singly_linked_lists(head1, head2)
print(cycle(new_head))
