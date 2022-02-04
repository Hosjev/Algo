class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recurse(node):
            nonlocal max_result
            if not node:
                return 0
            left = max(recurse(node.left), 0)
            right = max(recurse(node.right), 0)

            branch = node.val + left + right
            # Store possible local max
            max_result = max(max_result, branch)
            return node.val + max(left, right)

        # Prime
        max_result = float("-inf")

        # Logic
        recurse(root)

        return max_result


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(5)

    obj = Solution()
    print(obj.maxPathSum(t))
