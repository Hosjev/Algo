class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def _post_traverse(self, node, number: str):
        if not node:
            return ""
        number = self._post_traverse(node.next, number)
        number = number + str(node.val)
        return number

    def _make_list(self, summed):
        idx = 0
        next = None
        while idx != len(summed):
            node = ListNode(summed[idx])
            node.next = next
            next = node
            idx += 1
        return next

    def addTwoNumbers(self, l1, l2):
        added = int(self._post_traverse(l1, "")) + int(self._post_traverse(l2, ""))
        print(added)
        return self._make_list(str(added))


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(5)
    l2 = ListNode(3)
    l2.next = ListNode(1)
    obj = Solution()
    obj.addTwoNumbers(l1, l2)
