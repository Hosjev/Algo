# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        1. start with pointer
        2. declare head pointers
        3. move the pointers along
        4. return winning head
        The memory efficient "in-place" method
        """
        def merge_SLLs(head1, head2):
            H1 = head1
            H2 = head2
            pointer = None

            while H1 and H2:
                if H1.val < H2.val:
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

            return head1 if head1.val < head2.val else head2


        # Main logic
        # Edge cases
        if not lists: return None
        if len(lists) == 1: return lists[0]

        # Start with valid head
        idx = None
        for obj in range(len(lists)):
            if lists[obj]:
                head = lists[obj]
                idx = obj + 1
                break

        if not idx: return None

        while not idx == len(lists):
            next_head = lists[idx]
            if next_head:
                head = merge_SLLs(head, next_head)
            idx += 1

        return head

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        The runtime efficient method
        """
        def make_singly_linked(sorted_SLLs):
            pointer = ListNode(sorted_SLLs[0])
            for idx in range(1, len(sorted_SLLs)):
                head = ListNode(sorted_SLLs[idx])
                head.next = pointer
                pointer = head
            return pointer


        def cycle_nodes(head, array):
            if not head:
                return
            else:
                cycle_nodes(head.next, array)
                array.append(head.val)
            return array


        # Main logic
        sorted_SLLs = []
        for head in lists:
            if head:
                sorted_SLLs += (cycle_nodes(head, []))

        sorted_SLLs.sort(reverse=True)
        return make_singly_linked(sorted_SLLs) if sorted_SLLs else None



def cycle(head):
    if not head:
        return
    else:
        print(head.val)
        cycle(head.next)



# This version below reconstructs "in-place" ie--runtime suffers but O(S) better
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

k = [head1, head2, head3]
#k = [[], []]
#head_stupid = ListNode(1)
#k = [None, head_stupid]
# 1->1->2->3->4->4->5->6
#s = Solution()
#new_head = s.mergeKLists(k)
#print(cycle(new_head))

# RT efficient
s = Solution()
nh = s.mergeKLists(k)
print(cycle(nh))
