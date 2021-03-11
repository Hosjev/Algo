# def _loop(self, node1, node2, node_answer, carryover=0):
#      # starting at each head
#      # create head and pass any carryover
#      print(node1.value, node2.value)
#       local_sum = node1.value + node2.value + carryover
#        if local_sum > 9:
#             carryover = local_sum - 10
#             ans_value = carryover
#         else:
#             ans_value = local_sum
#         node_answer = LinkedList(ans_value)
#         self._loop(node1.next, node2.next, node_answer.next, carryover)
#         return node_answer

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def _loop(node1, node2, answer, carryover=0):
    # starting at each head
    # I'm overwriting head everytime!!!???
    value_one = _single_loop(node1)
    value_two = _single_loop(node2)
    print(value_one, value_two, carryover)
    local_sum = value_one + value_two + carryover
    if local_sum > 9:
        ans_value = local_sum - 10
        carryover = local_sum // 10
    else:
        carryover = 0
        ans_value = local_sum
    value = ans_value
    print(value)
    if not node1 and not node2:
        print("returning")
        pretty_print(answer)
        return answer
    elif not node1:
        print("reached 1")
        node1 = LinkedList(0)
    elif not node2:
        print("reached 2")
        node2 = LinkedList(0)
    answer.next = LinkedList(0)
    _loop(node1.next, node2.next, answer.next, carryover)


def _single_loop(node):
    if not node:
        return 0
    return node.value


def sumOfLinkedListsM(linkedListOne, linkedListTwo):
    # Write your code here.
    answer = LinkedList(None)
    _loop(linkedListOne, linkedListTwo, answer, 0)
    return answer


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # In this version, we're essentially cheating by priming
    # the new linked list with 0, then returning the real head.next
    # Always use WHILE with LL's, as recursion seems to overwrite the object
    # OR I'm not using pointers right
    # POINTERS are a way for your program to say: THIS OBJ IN MEMORY
    # you MUST use pointers in nested objects

    newLL = LinkedList(0)
    pointer = newLL  # head memory reference
    carryover = 0

    node1 = linkedListOne
    node2 = linkedListTwo
    while node1 or node2 or carryover != 0:
        value_one = node1.value if node1 else 0
        value_two = node2.value if node2 else 0
        local_sum = value_one + value_two + carryover

        local_value = local_sum % 10
        tempNode = LinkedList(local_value)
        pointer.next = tempNode
        pointer = tempNode
        carryover = local_sum // 10

        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    return newLL.next


def pretty_print(node):
    if not node:
        return
    print("My current node value:", node.value)
    pretty_print(node.next)


ll1 = LinkedList(2)
ll1.next = LinkedList(4)
ll1.next.next = LinkedList(7)
ll1.next.next.next = LinkedList(1)
ll2 = LinkedList(9)
ll2.next = LinkedList(4)
ll2.next.next = LinkedList(5)

print("Pre-run memory addr: ", ll1, ll2)
nl = sumOfLinkedLists(ll1, ll2)
print(nl)
pretty_print(nl)
