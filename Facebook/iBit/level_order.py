class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def levelOrder(self, A):
            # Prime
            stack = []
            bfs_hash = {}
            stack.append((1, A))
            while stack:
                level, node = stack.pop(0)
                if not level in bfs_hash:
                    bfs_hash[level] = [node.val]
                else: bfs_hash[level].append(node.val)
                if node.left: stack.append((level + 1, node.left))
                if node.right: stack.append((level + 1, node.right))

            return list(bfs_hash.values())


if __name__ == "__main__":
    # Layer 1
    tree = TreeNode(1)
    # Layer 2
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    # Layer 3
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    # Layer 4
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)

    #tree = TreeNode(1)
    #tree.left = TreeNode(2)
    print(Solution().levelOrder(tree))
