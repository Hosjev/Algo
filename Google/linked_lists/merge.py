class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        control_head = lists[0]
        idx = 1
        while idx < len(lists):
            orig_h1 = control_head
            orig_h2 = lists[idx]
            # 3 pointers
            h1, h2 = orig_h1, orig_h2
            pointer = None
            while h1 and h2:
                if h1.val < h2.val:
                    pointer = h1
                    h1 = h1.next
                else: # h2 >= h1
                    if pointer:
                        pointer.next = h2
                    pointer = h2
                    h2 = h2.next
                    pointer.next = h1
            # resolve dangling h2
            if not h1: pointer.next = h2
            control_head = orig_h2 if orig_h2.val <= orig_h1.val else orig_h1
            idx += 1
        return [control_head]


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(5)

    obj = Solution()
    new = obj.mergeKLists([l1, l2, l3])
    print(new[0].val)
