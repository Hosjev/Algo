class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class SumLL:

    def obj_int(self, node, string):
        if not node:
            return ""
        string = self.obj_int(node.next, string)
        string += str(node.value)
        return string

    def obj_sum_ll(self, string):
        idx = 0
        next = None
        while idx != len(string):
            node = Node(string[idx])
            node.next = next
            next = node
            idx += 1
        return next

    def sum_objects(self, head1, head2):
        # Edge Case
        if not head1 and not head2: return

        int_1, int_2 = self.obj_int(head1, ""), self.obj_int(head2, "")
        if not int_1: int_1 = 0
        if not int_2: int_2 = 0
        return self.obj_sum_ll(str(int(int_1) + int(int_2)))


def main():
    h1 = Node(6)
    h1.next = Node(5)
    h2 = Node(3)
    h2.next = Node(2)
    a = SumLL().sum_objects(h1, h2)


main()
