#!/usr/bin/python3.7

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def empty(self):
        return self.size == 0

    def peek(self):
        if self.empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


class StackSorter(Stack):
    def sort(self):
        buffer_stack = Stack()
        while not self.empty():
            obj = self.pop()
            if buffer_stack.empty() or \
               obj < buffer_stack.peek():
                buffer_stack.push(obj)
            else:
                while not buffer_stack.empty() and \
                          obj > buffer_stack.peek():
                    self.push(buffer_stack.pop())
                buffer_stack.push(obj)
        return buffer_stack


def buffer_array(obj) -> list:
    arr = list()
    while not obj.empty():
        item = obj.pop()
        arr.append(item)
    return arr

def main():
    from random import randint
    obj = StackSorter()
    [ obj.push(randint(0, 9)) for _ in range(10) ]
    #[ obj.push(i) for i in [4,3,1,2] ]
    stack_sorted = obj.sort()
    listified = buffer_array(stack_sorted)
    print(listified)

main()
