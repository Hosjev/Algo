"""
Return longest contiguous edge path.


Input:
    tree
Output:
    integer

** calc both diameter and depth
"""
import time


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class NodeData:
    """
    Someplace to track data as we recurse
    """

    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameter(tree):
    # recursively call function to calc both
    # length of path and node depth
    return dfsTree(tree).diameter


def dfsTree(node):
    if not node:
        return NodeData(0, 0)

    left_branch = dfsTree(node.left)
    right_branch = dfsTree(node.right)

    longestPath = left_branch.height + right_branch.height
    localDiameter = max(left_branch.diameter, right_branch.diameter)
    currentDiameter = max(longestPath, localDiameter)
    currentHeight = max(left_branch.height,
                        right_branch.height) + 1  # plus myself

    return NodeData(currentDiameter, currentHeight)


def tree1():
    # build tree
    tree = BST(10)
    # left side
    tree.left = BST(4)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(5)
    # right side
    tree.right = BST(17)
    tree.right.right = BST(19)
    tree.right.right.left = BST(18)
    return tree


def tree2():  # 6
    # build tree
    tree = BST(1)
    tree.left = BST(3)
    tree.left.left = BST(7)
    tree.left.left.left = BST(8)
    tree.left.left.left.left = BST(9)
    tree.left.right = BST(4)
    tree.left.right.right = BST(5)
    tree.left.right.right.right = BST(6)
    tree.right = BST(2)
    return tree


def tree3():  # 4
    tree = BST(1)
    tree.left = BST(2)
    tree.right = BST(3)
    tree.right.left = BST(6)
    tree.right.right = BST(7)
    tree.left.left = BST(4)
    tree.left.right = BST(5)
    return tree


if __name__ == "__main__":
    # build tree
    tree = tree2()

    print(binaryTreeDiameter(tree))
