# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lca(self, root, B, C):
        def bst_search(node, arr, target):
            if not node:
                return None
            local_arr = arr + [node.val]
            #if node.val == target:
            if node == target:
                return local_arr
            ans = bst_search(node.left, local_arr, target)
            if not ans:
                ans = bst_search(node.right, local_arr, target)
            return ans

        def equalize(b, c):
            if len(b) < len(c):
                c = c[0:len(b)]
            if len(b) > len(c):
                b = b[0:len(c)]
            return b, c

        # Main - steps
        b = bst_search(root, [], B)
        c = bst_search(root, [], C)
        # Early exit
        if not b or not c: return -1
        # Equalize each int
        b, c = equalize(b, c)
        # Then work up from that level
        p = len(b) - 1
        nodeB = b[-1]
        nodeC = c[-1]
        while nodeB != nodeC:
            p -= 1
            nodeB = b[p]
            nodeC = c[p]
        return nodeB


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
    print(Solution().lca(t, t.left.left, t.right.right))
    #print(Solution().lca(t, 5, 1))
    #print(Solution().lca(t, 5, 4))
    #print(Solution().lca(t, 5, 9))
