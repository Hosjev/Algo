#!/usr/bin/python3.7

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

class StackSorter(Stack):
    def sort(self):
        buffer_stack = Stack()
        while not self.is_empty():
            obj = self.pop()
            if buffer_stack.is_empty() or \
               obj >= buffer_stack.peek():
                buffer_stack.push(obj)
            else:
                while not buffer_stack.is_empty() and \
                          obj < buffer_stack.peek():
                    self.push(buffer_stack.pop())
                buffer_stack.push(obj)
        return buffer_stack


def buffer_array(obj) -> list:
    arr = list()
    while not obj.is_empty():
        item = obj.pop()
        arr.append(item)
    return arr

def main():
    from random import randint
    obj = StackSorter()
    [ obj.push(randint(0, 9)) for _ in range(10) ]
    stack_sorted = obj.sort()
    listified = buffer_array(stack_sorted)
    print(listified)

main()
