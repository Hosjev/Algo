"""
Write function that takes Binary Tree and returns list of its branch sums ordered from
leftmost branch to rightmost branch.
Input:
    tree =   1
           /   \
          2     3
         / \   / \
        4   5 6   7
       / \ /
      8  9 10
Output:
    [15, 16, 18, 10, 11]

*branch sum is sum of values in BT branch
*a branch is a path of nodes starting at root, ending at leaf
*each tree has int value, left and right node
*child nodes can be BT themselves or None (so L & R or None)
"""

def branchSums(tree):
    # Run a DFS that sums at branch split and recursively gives
    #  sum to next depth
    node_sums = []

    # Say we reach 8, we sum but have no L/R
    def inner_sum(node, n_sum): # O(N)
        n_sum += node.value

        # Did we reach leaf?
        if not (node.left or node.right):
            node_sums.append(n_sum)

        # Favor left first
        if node.left:
            inner_sum(node.left, n_sum)
        if node.right:
            inner_sum(node.right, n_sum)

    inner_sum(tree, 0)
    return node_sums


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    # Layer 1
    tree = BinaryTree(1)
    # Layer 2
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    # Layer 3
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    # Layer 4
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)
    tree.left.right.left = BinaryTree(10)


    print(branchSums(tree))
