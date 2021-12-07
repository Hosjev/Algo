class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def _traverse(self, node, parent = None):
        if not node:
            return parent
        return self._traverse(node.left, node) and \
               self._traverse(node.right, node)

    def flatten(self, root) -> None:
        """ 1. if Left branch, find tail
            2. detach at root/node of Right
            3. move Left to Right, nullify Left
            4. reattach orig Right to tail
        """
        if not root: return root
        head, node = root, root
        while node:
            if node.left:
                tail = self._traverse(node.left)
                detach = node.right
                node.right = node.left
                tail.right = detach
                node.left = None
                node = node.right
            else:
                node = node.right
        return head


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right = TreeNode(5)
    t.right.right = TreeNode(6)
    nt = Solution().flatten(t)
    while nt:
        print(nt.val)
        nt = nt.right
