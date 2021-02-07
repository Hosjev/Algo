"""
Write 3 functions that take in BST and an empty array.
Traverse the BST and its nodes' values to the input array.
The 3 functions should traverse the tree using in-order, pre-order, post-order.
In that order.
Input:
    tree =  10
           /  \
          5    15
         / \    \
        2   5    22
       /
      1
    array = []
Output:
    in_order: [1, 2, 5, 5, 10, 15, 22]
    pre_order: [10, 5, 2, 1, 5, 15, 22]
    post_order: [1, 2, 5, 5, 22, 15, 10]

* follow Bst properties
answer - O(N)ST
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree, array):
    # Return nothing but nulls and simply append as callback
    if not tree:
        return None
    inOrderTraverse(tree.left, array)
    #print(tree.value) # None answers then the 1st callback
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array # This gets returned up the stack though we have no 'state'


def preOrderTraverse(tree, array):
    # Left to right
    if not tree:
        return None
    #print(tree.value)
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # [1, 2, 6, 5, 22, 15, 10]
    # bottom up
    if not tree:
        return None
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    #print(tree.value)
    array.append(tree.value)
    return array


def tree1():
    # True
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.right.left = BST(14)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(6)
    tree.right.right = BST(22)
    return tree


def tree3():
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.left.left = BST(2)
    tree.left.right = BST(6)
    return tree


if __name__ == "__main__":

    # My nested tree object
    tree = tree1()

    print(inOrderTraverse(tree, []))
    print(preOrderTraverse(tree, []))
    print(postOrderTraverse(tree, []))
