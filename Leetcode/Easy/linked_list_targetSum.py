class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Broken
    def _traverse(self, left, right, currentSum, targetSum):
        if not left and not right:
            print(currentSum)
            # Eval
            if currentSum == targetSum:
                return True
            else:
                return False
        if not left or not right: return False
        return self._traverse(left.left, left.right, currentSum + left.val, targetSum) or \
               self._traverse(right.left, right.right, currentSum + right.val, targetSum)
    
    def hasPathSum(self, root, targetSum: int) -> bool:
        result = self._traverse(root.left, root.right, root.val, targetSum)
        return result



if __name__ == "__main__":
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.right = TreeNode(8)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)
    t.right.left = TreeNode(13)
    t.right.right = TreeNode(4)
    t.right.right.right = TreeNode(1)
    print(Solution().hasPathSum(t, 22))
        
