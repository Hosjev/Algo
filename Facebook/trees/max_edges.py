class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Prime
        self.edges = float("-inf")

        def recurse(node):
            if not node:
                return 0
            left = recurse(node.left)
            right = recurse(node.right)

            local_branch = left + right
            self.edges = max(self.edges, local_branch)
            return 1 + max(left, right)

        # Logic
        recurse(root)

        return self.edges


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(5)
    t.left.left.left = TreeNode(4)
    t.left.left.right = TreeNode(3)
    t.left.right.left = TreeNode(5)
    t.left.right.right = TreeNode(5)

    obj = Solution()
    print(obj.diameterOfBinaryTree(t))
