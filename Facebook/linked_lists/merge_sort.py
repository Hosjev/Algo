class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    """ To reach O(N) use 3 pointers and control via list1 """
    def mergeTwoLists(self, list1, list2):
        # Edge Case(s)
        if not bool(list1): return list2
        if not bool(list2): return list1
        
        # Prime
        head1, head2 = list1, list2 
        pointer = None
        
        # Logic
        while head1 and head2:
            if head1.val < head2.val:
                pointer = head1
                head1 = head1.next
            else:
                if pointer:
                    pointer.next = head2
                pointer = head2
                head2 = head2.next
                pointer.next = head1

        # Dangling participle
        if not head1: pointer.next = head2
            
        return list2 if list2.val <= list1.val else list1


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    obj = Solution()
    print(obj.mergeTwoLists(l1, l2))
