"""
Write a function that takes Bst and returns whether valid.
Input:
    object builds and method calls
Output:
    True/False

* follow Bst properties
O(N)T / O(d)S -- d is depth (all nodes end up on the call stack)
"""
import time


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def cycle(self, parent, direction=None):
        if parent: print(f"Parent is: {parent.value}")
        else: print(f"Starting at None")
        print(f"node: {self.value}:{direction}\n")
        if self.left: self.left.cycle(self, "left")
        if self.right: self.right.cycle(self, "right")


def validateBst(tree):
    answer = [True]

    def inner_valid(tree, answer):

        if tree.left:
            #print(f"...L: {tree.left.value}")
            if (tree.value) < (tree.left.value):
                answer[0] = False
            inner_valid(tree.left, answer)
        if tree.right:
            #print(f"...R: {tree.right.value}")
            if (tree.value) > (tree.right.value):
                answer[0] = False
            inner_valid(tree.right, answer)


    inner_valid(tree, answer)
    return answer[0]


def validateBst(tree):
    # Feed the external validation: tree, neg int, pos int
    return recur_validation(tree, float("-inf"), float("inf"))

def recur_validation(tree, min_v, max_v):
    if not tree:
        # Reached empty node
        return True
    if (tree.value < min_v) or (tree.value >= max_v):
        return False
    down_result = recur_validation(tree.left, min_v, tree.value)
    return down_result and recur_validation(tree.right, tree.value, max_v)


def tree1():
    # True
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.left.left = BST(2)
    tree.left.right = BST(5)
    tree.left.left.left = BST(1)
    tree.right.left = BST(13)
    tree.right.right = BST(22)
    tree.right.left.right = BST(14)
    return tree


def tree2():
    # False
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.left.left = BST(2)
    tree.left.right = BST(5-2)
    tree.left.right.right = BST(11)
    tree.left.left.left = BST(1)
    tree.right.right = BST(22)
    return tree


def tree3():
    # True
    tree = BST(10)
    tree.left = BST(5)
    tree.right = BST(15)
    tree.left.left = BST(2)
    tree.left.right = BST(5)
    return tree


if __name__ == "__main__":

    # My nested tree object
    tree = tree2()
    #tree = tree3()

    #print(tree.cycle(None))
    print(validateBst(tree))
