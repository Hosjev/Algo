class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseLL(self, head, m, n):
        """
        Input: linked list, m pos, n pos
        Output: linked list reversed from POSITION m->n
        Note: m can be absent and list not sorted
        """
        def pos_check(node, m, n):
            count = 1
            res = []
            while node:
                if count == m:
                    res.append("m")
                if count == n:
                    res.append("n")
                    break
                node = node.next
                count += 1
            return res

        # Edge Case(s)
        res = pos_check(head, m, n)
        if not len(res) == 2 or \
            not sorted([m, n]) == [m, n]:
            return head

        # Prime
        node = head
        prev = node
        count = 0

        # Outer while
        while node:
            count += 1
            if count == m:
                cur = node
                tail = None
                # Inner while
                while True:
                    future = cur.next
                    cur.next = tail
                    tail = cur
                    cur = future
                    if count == n:
                        # Reconnect parts
                        if not prev.val == node.val:
                            prev.next = tail
                        node.next = future
                        break
                    count += 1
            prev = node
            node = node.next

        return tail if m == 1 else head


def cycle(node):
    if not node:
        return
    print(node.val)
    cycle(node.next)


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
m = 2
n = 4
a = Solution().reverseLL(h, m, n)
cycle(a)


#A : [ 17 -> 94 -> 28 -> 18 -> 93 -> 27 -> 13 -> 44 -> 70 -> 65 -> 20 -> 54 -> 62 -> 68 -> 41 -> 86 -> 49 -> 2 -> 19 -> 80 -> 4 -> 69 -> 48 -> 38 -> 35 -> 5 -> 50 -> 90 -> 58 -> 64 -> 32 -> 73 -> 72 -> 82 -> 79 -> 92 -> 87 -> 8 -> 37 -> 9 -> 16 -> 56 -> 36 -> 76 -> 43 -> 61 -> 46 -> 95 -> 3 -> 25 -> 15 -> 53 -> 6 -> 99 -> 96 -> 71 -> 57 -> 100 -> 12 ]
#3 44
#97 -> 63 -> 89 -> 34 -> 82 -> 95 -> 4 -> 70 -> 14 -> 41 -> 38 -> 83 -> 49 -> 32 -> 68 -> 56 -> 99 -> 52 -> 33 -> 54 ]
#97 -> 63 -> 89 -> 34 -> 82 -> 95 -> 4 -> 70 -> 14 -> 41 -> 38 -> 83 -> 68 -> 32 -> 49 -> 56 -> 99 -> 52 -> 33 -> 54 
#13 15
#97 -> 63 -> 89 -> 34 -> 82 -> 95 -> 4 -> 70 -> 14 -> 41 -> 38 -> 83 -> 49 -> 32 -> 68 -> 56 -> 99 -> 52 -> 33 -> 54 

