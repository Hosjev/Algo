class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def _dfs_tree(self, node, placeholder, result):
        placeholder += str(node.val) + "->"
        if node.left:
            self._dfs_tree(node.left, placeholder, result)
        if node.right:
            self._dfs_tree(node.right, placeholder, result)
        if not node.left and not node.right: # pure leaf
            result.append(placeholder.rstrip("->"))
        return result
    
    def binaryTreePaths(self, root) -> list:
        # Edge Case(s)
        if not root: return [""]
        
        # Prime
        result = list()
                
        # Logic
        return self._dfs_tree(root, "", result)


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(5)
    obj = Solution()
    print(obj.binaryTreePaths(t))
