class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Reading from left to right, we take furthest R
        #   using a BFS and a buffer
        if not root: return []

        # Prime
        tree_buffer = [root]
        unobscured = list() # by R

        while bool(tree_buffer):
            # Empty buffer
            unobscured.append(tree_buffer[-1].val)
            temp = list()
            for node in tree_buffer:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            tree_buffer = temp
        return unobscured
