class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, nodeA, nodeB):
        if not nodeA and not nodeB:
            return True
        if not nodeA or not nodeB:
            return False
        if nodeA.val != nodeB.val:
            return False
        return self._traverse(nodeA.left, nodeB.left) and \
               self._traverse(nodeA.right, nodeB.right)
        
    def isSameTree(self, p, q) -> bool:
        result = self._traverse(p, q)
        return result
        


if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(1)

    b = TreeNode(1)
    b.left = TreeNode(2)

    print(Solution().isSameTree(a, b))
