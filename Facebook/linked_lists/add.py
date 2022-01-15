from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def _make_list(self, linked_sum: str) -> Optional[ListNode]:
        # Run an iterative algorithm O(N)
        tail = None
        idx = 0
        while idx != len(linked_sum):
            node = ListNode(int(linked_sum[idx]))
            node.next = tail
            tail = node
            idx += 1
        return tail

    def _get_integer(self, ll: Optional[ListNode]) -> int:
        # Run an iterative algorithm O(N)
        linked_int = str()
        node = ll
        while node:
            linked_int = str(node.val) + linked_int
            node = node.next
        return int(linked_int)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Guaranteed no leading zeros
        # Edge Case(s)
        if not l1: return l2
        if not l2: return l1

        # Logic
        sum_linked = (self._get_integer(l1) + self._get_integer(l2))
        return self._make_list(str(sum_linked))


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    obj = Solution()
    ll = obj.addTwoNumbers(l1, l2)
