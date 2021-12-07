class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def push(self, val: int) -> None:
        node = Node(val)
        next = self.head.next
        self.head.next = node
        node.next = next
        self.size += 1
        self._eval_min(node)
        
    def pop(self) -> None:
        if not self.size: return
        node = self.head.next
        self.head.next = node.next
        self._eval_min(node)
        self.size -= 1
        return node.value

    def top(self) -> int:
        return None if not self.size else self.head.next.value
        
        

class MinStack(Stack):

    def __init__(self):
        super().__init__()
        self.mins = Stack()

    def _eval_min(self, node):
        if node.value < getMin():
            self.mins_stack.push(node.val)

    def getMin(self) -> int:
        return self.mins_stack.top()
        

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
