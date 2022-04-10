# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        from collections import defaultdict
        stack = []
        stack.append((0, root))
        levels = defaultdict(list)
        
        # Step 1
        while stack:
            key, node = stack.pop()
            if node:
                levels[key].append(node.val)
            else: levels[key].append(None)
            if node: stack.append((key+1, node.left))
            if node: stack.append((key+1, node.right))
        # Step 2
        for k,v in levels.items():
            if k != 0:
                if len(v) % 2 != 0 or \
                  v[:int(len(v) / 2)] != [i for i in reversed(v[int(len(v) / 2):])]:
                    return False
        return True


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(3)
    print(Solution().isSymmetric(t))

