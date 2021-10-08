class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def ll_iHelper(self, node):
        # Iterative version
        string = ""
        while node:
            string += str(node.val)
            node = node.next
        return string
        

    def ll_iMaker(self, summed_ll):
        # Iterative version - return (467)
        idx = len(summed_ll) - 1
        next = None
        while not idx < 0:
            node = ListNode(int(summed_ll[idx]))
            node.next = next
            next = node
            idx -= 1
        return node


    def reverse_string(self, num):
        return "".join(j for j in reversed([i for i in num]))


    def addTwoNumbers(self, A, B):
        # Edge Case(s)
        if A.val == 0:
           return B
        if B.val == 0:
           return A

        # Prime
        sum_1 = self.reverse_string(self.ll_iHelper(A))
        sum_2 = self.reverse_string(self.ll_iHelper(B))
        sum_of_1_2 = str(int(sum_1) + int(sum_2))
        return self.ll_iMaker(self.reverse_string(sum_of_1_2))




ll1 = ListNode(1)
ll1.next = ListNode(6)
ll1.next.next = ListNode(2)
ll2 = ListNode(3)
ll2.next = ListNode(0)
ll2.next.next = ListNode(5)
print(Solution().addTwoNumbers(ll1, ll2))

ll1 = ListNode(9)
ll1.next = ListNode(9)
ll1.next.next = ListNode(1)
ll2 = ListNode(1)
print(Solution().addTwoNumbers(ll1, ll2).next.next.val)

ll1 = ListNode(1)
ll1.next = ListNode(0)
ll1.next.next = ListNode(1)
ll2 = ListNode(0)
print(Solution().addTwoNumbers(ll1, ll2).val)
