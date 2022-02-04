class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right >= 2:
                self.result = current_node
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.result


if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(5)
    t.right = TreeNode(1)
    t.left.left = TreeNode(6)
    t.left.right = TreeNode(2)
    t.right.left = TreeNode(0)
    t.right.right = TreeNode(8)
    t.left.right.left = TreeNode(7)
    t.left.right.right = TreeNode(4)
    obj = Solution()
    print(obj.lowestCommonAncestor(t, t.left.left, t.right.right).val)
