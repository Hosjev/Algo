class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def isValidBST(self, A):
        def recur_validation(tree, min_v, max_v):
            if not tree:
                # Reached empty node
                return True
            if (tree.val < min_v) or (tree.val >= max_v):
                return False
            left = recur_validation(tree.left, min_v, tree.val)
            return left and recur_validation(tree.right, tree.val, max_v)
        return recur_validation(A, float("-inf"), float("inf"))


def tree1():
    # True
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(5)
    tree.left.right.right = TreeNode(9)
    tree.left.left.left = TreeNode(1)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(22)
    tree.right.left.right = TreeNode(14)
    return tree


def tree2():
    # False
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(5-2)
    tree.left.right.right = TreeNode(11)
    tree.left.left.left = TreeNode(1)
    tree.right.right = TreeNode(22)
    return tree


def tree3():
    # True
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(5)
    return tree


if __name__ == "__main__":

    # My nested tree object
    tree = tree2()

    print(Solution().isValidBST(tree))
