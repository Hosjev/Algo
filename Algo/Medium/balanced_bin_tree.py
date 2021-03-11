"""
Write a function that takes in binary tree root. Return boolean whether tree is balanced.


Input:
    tree =  1
           /  \
          2    3
         / \    
        4   5    
       /
      6

Output:
    false

** count "levels" from root, L/R branches
"""
import time


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class NodeData:
    def __init__(self, height):
        self.height = height
        self.balance = True


def heightBalancedBinaryTree(tree):
    # Write your code here.
    # time complexity could be improved by changing
    # this function into iterative calls
    # and BREAK when false is reached
    return exploreBranches(tree, True)[1]


def exploreBranches(node, flag):
    # recursive calls
    if not node:
        return NodeData(0), flag

    # go left
    left_branch, flag = exploreBranches(node.left, flag)
    # go right
    right_branch, flag = exploreBranches(node.right, flag)

    height_difference = abs(left_branch.height - right_branch.height)
    if height_difference > 1:
        # just pick a side
        flag = False

    height_max = max(left_branch.height,
                     right_branch.height) + 1  # plus myself

    return NodeData(height_max), flag


def tree1():  # false
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


def tree2():  # true
    # build tree
    tree = BST(1)
    # left side
    tree.left = BST(2)
    tree.right = BST(4)
    return tree


def treeRoot():
    return BST(0)


def tree3():  # false
    # build tree
    #          1
    #        /    \
    #       2      3
    #      / \      \
    #     4   5      6
    #        / \    /  \
    #       7   8  9   10
    tree = BST(1)
    # left side
    tree.left = BST(2)
    tree.right = BST(3)
    tree.left.left = BST(4)
    tree.left.right = BST(5)
    tree.right.right = BST(6)
    tree.left.right.left = BST(7)
    tree.left.right.right = BST(8)
    tree.right.right.left = BST(9)
    tree.right.right.right = BST(10)
    return tree


if __name__ == "__main__":
    # build tree
    tree = tree3()
    #tree = treeRoot()

    print(heightBalancedBinaryTree(tree))
