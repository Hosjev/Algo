import sys
sys.path.append("/home/wendiw/Xenial/PythonPlay/Facebook")
from linked_list_funcs import Node, LinkedList

class LLDups(LinkedList):

    def remove_dups(self, node):
        # ECs 0-1 return node
        unique = dict()
        head = node 
        while node.next:
            unique[node.value] = 1
            while node.next and node.next.value in unique:
                node.next = node.next.next # skip it
            node = node.next
        return head
