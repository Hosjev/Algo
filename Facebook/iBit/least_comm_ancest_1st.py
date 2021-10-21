# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
            def build_heap(A):
                stack = []
                stack.append(A)
                heap = []
                while stack:
                    node = stack.pop(0)
                    val = None if not node else node.val
                    heap.append(val)
                    if node:
                        if node and not node.left:
                            stack.append(None)
                        else: stack.append(node.left)
                        if node and not node.right:
                            stack.append(None)
                        else: stack.append(node.right)
                return heap

            def build_array(heap, n):
                # Backward
                arr = [heap[n]]
                while n != 0:
                    if n % 2 == 0:
                        n = int((n - 2) / 2)
                    else:
                        n = int((n - 1) // 2)
                    arr = [heap[n]] + arr
                return arr

            def equalize(b, c):
                if len(b) < len(c):
                    c = c[0:len(b)]
                if len(b) > len(c):
                    b = b[0:len(c)]
                return b, c

            # Main - steps
            # Build heap-like struct from BFS
            heap = build_heap(A)
            # Get depth of each int
            try:
                B_arr = build_array(heap, heap.index(B))
                C_arr = build_array(heap, heap.index(C))
            except ValueError:
               return -1
            # equalize each int
            B_arr, C_arr = equalize(B_arr, C_arr)
            # then work up from that level
            p = len(B_arr) - 1
            nodeB = B_arr[-1]
            nodeC = C_arr[-1]
            while nodeB != nodeC:
                p -= 1
                nodeB = B_arr[p]
                nodeC = C_arr[p]
            return nodeB


t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.left.left = TreeNode(6)
t.left.right = TreeNode(2)
t.right.left = TreeNode(0)
t.right.right = TreeNode(8)
t.left.right.left = TreeNode(7)
t.left.right.right = TreeNode(4)
print(Solution().lca(t, 6, 4))
