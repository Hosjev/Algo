"""
Write a function that takes binary tree with parent element and a node value. Find the "next" node after given value as would appear in an in-order traversal.


Input:
    tree =  1
           /  \
          2    3
         / \    
        4   5    
       /
      6
    node = 5
    ** IOT is [6, 4, 2, 5, 1, 3]
Output:
    integer

** why is parent important?
** just input tree into inOrder func and return val[i+1]
"""
import time


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    answer = None
    array = inOrderTraverse(tree, [])
    # print(array)
    try:
        answer = array[array.index(node) + 1]
    except IndexError:
        pass

    return None if not answer else answer


def inOrderTraverse(node, array):
    # left bottom to right by branch
    if not node:
        return

    inOrderTraverse(node.left, array)
    array.append(node.value)
    inOrderTraverse(node.right, array)

    return array  # keep moving this up the stack


def tree1():
    # build tree
    tree = BST(1)
    # left side
    tree.left = BST(2)
    tree.left.left = BST(4)
    tree.left.left.left = BST(6)
    tree.left.right = BST(5)
    # right side
    tree.right = BST(3)
    return tree


if __name__ == "__main__":
    # build tree
    tree = tree1()

    print(findSuccessor(tree, 5))
