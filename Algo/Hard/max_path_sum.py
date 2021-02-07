"""
Write a function that takes in a BST and returns its max path sum.

Input:
    tree_obj = 
             1
           /   \
          2     3
         / \   / \
        4   5 6   7

Output:
    18 # 5 2 1 3 7

answer - O(N)T / O(N)S
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def maxPathSum(tree):
    # Call recursion

    tree_max = max_path(tree)

    return tree_max


def max_path(node):
    if not node:
        return (float("-inf"), float("-inf"))

    open_left_branch, left_local = max_path(node.left)
    open_right_branch, right_local = max_path(node.right)

    # The max surfacing from branches Including JUST myself (node)
    winner_branch = max(open_left_branch, open_right_branch)
    max_branches = max(winner_branch + node.value, node.value)

    # The max of the above, either the L/R branches or the current node
    #   compared to the the local triangle (which includes the branches)
    # *** If you have a fair and long non-negative number of nodes, this will
    # most likely always be the winner.
    sum_triangle = max(max_branches, open_left_branch + node.value + open_right_branch)

    # The max of the branches or the max of left and right running
    # non-contiguous lines for the previous caller
    running_max_local_sum = max(sum_triangle, left_local, right_local)

    return (max_branches, running_max_local_sum)




if __name__ == "__main__":

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    #tree = Node(1)
    #tree.left = Node(-1)
    #tree.right = Node(2)

    #tree = Node(1)
    #tree.left = Node(-5)
    #tree.right = Node(3)
    #tree.left.left = Node(6)

    print(maxPathSum(tree))
    # Why doesn't maxPath work on root node?
    # A last check max left + right or just left
