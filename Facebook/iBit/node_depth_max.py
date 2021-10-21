class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class Solution:
    def maxDepth(self, A):
        def node_depth(node):
            if not node:
                return 0
            left = node_depth(node.left)
            right = node_depth(node.right)
            return max(left, right) + 1

        return node_depth(A)



if __name__ == "__main__":
    # Layer 1
    tree = TreeNode(1)
    # Layer 2
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    # Layer 3
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    # Layer 4
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)

    print(Solution().maxDepth(tree))
