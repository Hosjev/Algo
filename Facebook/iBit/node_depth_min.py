class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, A):
            def bst_helper(node):
                if not node:
                    return 0
                left = bst_helper(node.left)
                right = bst_helper(node.right)
                if not left:
                    b_sum = (right) + 1
                if not right:
                    b_sum = (left) + 1
                if left and right:
                    b_sum = min(left, right) + 1
                return b_sum

            return bst_helper(A)


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
    #tree.right.right = TreeNode(7)
    # Layer 4
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)

    tree = TreeNode(1)
    #tree.left = TreeNode(2)
    print(Solution().minDepth(tree))
