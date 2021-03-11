"""
Given preOrder array, return tree with its matching node/object values.


Input:
    preOrder = [10, 4, 2, 1, 5, 17, 19, 18]
Output:
    tree

** in-order traversal (as seen above)
"""
import time


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        # eval each integer and keep sifting
        # until we find an available branch
        # BST--left=strictly less than
        #    --right=greater than/or/equal-to

        # We handle left first then right as else (satisfying >=)
        if (value < self.value):
            # if we have an available leaf, write it
            if not self.left:
                self.left = BST(value)
            # go further left
            else:
                self.left.insert(value)
        else:
            # if we have an available leaf, write it
            if not self.right:
                self.right = BST(value)
            # go further right
            else:
                self.right.insert(value)


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    # init with root
    tree = BST(preOrderTraversalValues[0])
    for idx in range(1, len(preOrderTraversalValues)):
        tree.insert(preOrderTraversalValues[idx])

    return tree


def preOrderTraverse(node, orderedArray):
    # pre-order means root, left branch (DESC) moving right
    if not node:
        return None

    orderedArray.append(node.value)
    preOrderTraverse(node.left, orderedArray)
    preOrderTraverse(node.right, orderedArray)
    # we do nothing w/our return but to move up stack
    return orderedArray


if __name__ == "__main__":
    preOrder = [10, 4, 2, 1, 5, 17, 19, 18]
    tree = reconstructBst(preOrder)
    print(tree)
    run = preOrderTraverse(tree, [])
    print("run?", run)
