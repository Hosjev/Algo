"""
Write a function that takes in a tree and returns kth largest value from root.

Input:
    tree = 1, 2, 3, 5, 5, 15, 17, 20, 22
    kth = 3
Output:
    17

** I think this is pre-order traversal (left branch then right DESC)
"""
import time


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    # create the in-order traversal
    # move backward thru the tree as array
    orderedTree = inOrderTraverse(tree, [])
    return orderedTree[len(orderedTree) - k]


def inOrderTraverse(node, orderedArray):
    if not node:
        return None

    inOrderTraverse(node.left, orderedArray)
    orderedArray.append(node.value)
    inOrderTraverse(node.right, orderedArray)
    # returned multiple times but ultimately up the stack to root
    # then to caller
    return orderedArray


if __name__ == "__main__":
    # build tree
    tree = BST(15)
    # left side
    tree.left = BST(5)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.left.right = BST(3)
    tree.left.right = BST(5)
    # right side
    tree.right = BST(20)
    tree.right.left = BST(17)
    tree.right.right = BST(22)

    print(findKthLargestValueInBst(tree, 3))
