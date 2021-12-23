class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def _middle(self, node):
        head1, slow, fast = node, node, node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return head1, prev, slow

    def _reverse(self, node):
        tail = None
        current = node
        while current:
            future = current.next
            current.next = tail
            tail = current
            current = future
        return tail

    def reorderList(self, head) -> None:
        """
        1. find middle
        2. reverse 2nd half
        3. merge the 2 with nodeA1, nodeB1...
        """
        # EC
        if not head.next.next: return head

        head1, h1_end, middle = self._middle(head)
        h1_end.next = None
        head2 = self._reverse(middle)
        # Merge
        if not head1.next:
            head1.next = head2
        else:
            pointer = head1
            future = head2
            while pointer and future:
                temp = pointer.next
                pointer.next = future
                pointer = future
                future = temp
        return head1


if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    ll.next.next.next.next.next = ListNode(6)
    obj = Solution()
    n_obj = obj.reorderList(ll)
