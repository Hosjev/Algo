"""
Write a BST class for binary search tree. The class should support:
  -inserting values
  -removing values
  -searching for values with the "contains" method
Note that you can't remove values from a single-node tree. EX-calling remove on a single node
tree results in no action.
Input:
    object builds and method calls
Output:
    only the contains method?

answer - best- O(log(N))T / O(1)S -- worst O(N)T
"""
import time


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # What about a method that makes an easy iterable object?
    # An object that all these methods can access?
    # No b/c the class is always returning self and the calling functions aren't looking for 2d arr

    def insert(self, value):
        # L < N <= R
        # This should really be called "adding_leaf" as
        # the logic lends itself to ONLY that w/o breaking BST rules
        # Keep trying until you find an available leaf
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
               self.right = BST(value)

        return self

    def remove(self, value, parent = None):
        # Two parts to this.
        # 1-find node to remove
        # 2-if it has L/R, find a replacement
        # To sum up: GRAB Smallest value in right subtree to use as replacement
        if value < self.value:
            if self.left: self.left.remove(value, self)
        elif value > self.value:
            if self.right: self.right.remove(value, self)
        else: # match
            if self.left and self.right:
                self.value = self.right.retrieve_leaf()
                self.right.remove(self.value, self)
            elif not parent:
                # The below does not apply to root node BECAUSE the above will always be true for 3 or more R/L binary tree
                if self.left: # we have 2 or more left only nodes
                    print(f"current val: {self.value}")
                    print(f"current val: {self.left.value}")
                    print(f"current val: {self.left.left}")
                    print(f"current val: {self.left.right}")
                    # Basically make all left the new root
                    # the left/rights below HAVE to be done in this order, as you're overwriting
                    #   self.left (and right)
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right:
                    # Basically make all right the new root
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else: # singleton
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right

        return self

    def retrieve_leaf(self):
        # Favor left after going right
        if not self.left:
            # if we've reached the end of going left, return the current node
            return self.value
        else:
            return self.left.retrieve_leaf()

    def contains(self, value):
        # Given the rules of BST, if we don't eventually get a match
        # we return false on a left or right turn that doesn't exist
        # Basically dead ends
        if value < self.value:
            if not self.left: return False
            else: return self.left.contains(value)
        elif value > self.value:
            if not self.right: return False
            else: return self.right.contains(value)
        else:
            return True

    def cycle(self, parent, direction=None):
        if parent: print(f"Parent is: {parent.value}")
        else: print(f"Starting at None")
        print(f"node: {self.value}:{direction}\n")
        if self.left: self.left.cycle(self, "left")
        if self.right: self.right.cycle(self, "right")




if __name__ == "__main__":

    # My nested tree object
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.left.left = BST(2)
    tree.left.right = BST(5)
    tree.left.left.left = BST(1)
    tree.right.left = BST(13)
    tree.right.right = BST(22)
    tree.right.left.right = BST(14)

    print(f"Contains: {tree.contains(14)}")
    print(tree.cycle(None))
    print(f"Insert: {tree.insert(12)}")
    print(f"Remove: {tree.remove(14)}")
    print(f"Remove: {tree.remove(15)}")
    print(f"Remove: {tree.remove(5)}")
    print(tree.cycle(None))

    tree = BST(10)
    print("Insert")
    tree.insert(5)
    tree.cycle(None)
    print("Remove")
    tree.remove(10)
    print("Contains")
    tree.contains(15)
