import sys
sys.path.append("/home/wendiw/Xenial/PythonPlay/Facebook")
from linked_list_funcs import Node, LinkedList

class LLPartition(LinkedList):

    def partition(self, node, num):
        before = LLPartition()
        after = LLPartition()
        curr = node.head.next
        while curr:
            if curr.value < num:
                before.append(curr.value)
            elif curr.value > num:
                after.append(curr.value)
            else: # equal
                mid = curr
            curr = curr.next

        bef_pointer = before.head
        while bef_pointer.next:
            bef_pointer = bef_pointer.next
        bef_pointer.next = mid
        mid.next = after.head.next
        return before


def main():
    linkedlist = LinkedList()
    linkedlist.insert(2)
    linkedlist.insert(15)
    linkedlist.insert(5)
    linkedlist.insert(12)
    linkedlist.insert(1)
    linkedlist.insert(9)
    linkedlist.insert(6)
    linkedlist.insert(8)
    new_linkedlist = LLPartition().partition(linkedlist, 6)
    new_linkedlist.print()

main()
