class StackError(Exception):
    pass


class Stack:
    """ Making a dynamic array of sorts """

    def __init__(self, num, size):
        """ num is length of array; size is depth of stack """
        self.num = num
        self.size = size
        self.pointers = [-1] * self.num # B/C 0 index
        self.array = [None] * self.num * self.size

    def abs_index(self, stack_index):
        return stack_index * self.size + self.pointers[stack_index]

    def push(self, stack_index, data):
        if self.pointers[stack_index] == self.size - 1:
            raise StackError("Stack is full")
        self.pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.array[array_index] = data

    def pop(self, stack_index):
        if self.array[stack_index] == -1:
            raise StackError("Stack is empty")
        array_index = self.abs_index(stack_index)
        data = self.array[array_index]
        self.array[array_index] = None
        self.pointers[stack_index] = -1
        return data


def main(num, size):
    s = Stack(num, size)
    s.push(0, "a")
    s.push(0, "b")
    s.push(0, "c")
    s.push(0, "d")
    s.push(0, "e")
    s.push(0, "f")
    print(s.array)


main(2, 5)
