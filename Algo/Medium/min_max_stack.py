"""
Write a class for a Min Max stack. As below. All class methods, when considered independently, should run in constant time and space.

Input:
    MinMaxStack():
    push(5)
    getMin(): 5
    getMax(): 5
    peek(): 5
    push(7): 
    getMin(): 5
    getMax(): 7
    peek(): 7
    push(2): 
    getMin(): 2
    getMax(): 7
    peek(): 2
    pop(): 2
    pop(): 7
    getMin(): 5
    getMax(): 5
    peek(): 5


O(1)T | O(1)S -- all operations are constant time
"""
import time


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []

    def peek(self):
        # Write your code here.
        return self.stack[-1] if len(self.stack) > 0 else None

    def pop(self):
        # Write your code here.
        last_item = self.stack.pop()
        trash = self.min_max.pop()
        return last_item

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        # Get current min/max and update stack tuples
        self.prime_mm()
        self.update_min(number)
        self.update_max(number)
        
    def getMin(self):
        # Write your code here.
        # This code evaluates current min - tuple[0] of last index
        # and updates accordingly
        return self.min_max[-1][0] if len(self.min_max) > 0 else None

    def getMax(self):
        # Write your code here.
        # This code evaluates current max - tuple[1] of last index
        # and updates accordingly
        return self.min_max[-1][1] if len(self.min_max) > 0 else None

    def prime_mm(self):
        self.min_max.append( [float("inf"), float("-inf")] )
        #self.min_max.append( (0, 0) )

    def update_min(self, number):
        # Handle edges cases
        # If there are NO items, do nothing as the method is called by push.
        # If there is ONE item
        if len(self.min_max) == 1:
            current_min = self.min_max[-1][0]
        else:
            current_min = self.min_max[-2][0]
        new_min = min(current_min, number)
        self.min_max[-1][0] = new_min

    def update_max(self, number):
        # Handle edge cases
        # If there are NO items, do nothing as the method is called by push.
        # If there is ONE item
        if len(self.min_max) == 1:
            current_max = self.min_max[-1][1]
        else:
            current_max = self.min_max[-2][1]
        new_max = max(current_max, number)
        self.min_max[-1][1] = new_max
        



if __name__ == "__main__":

    # Instantiate stack
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print("pushing")
    stack.push(7)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print("pushing")
    stack.push(2)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())

