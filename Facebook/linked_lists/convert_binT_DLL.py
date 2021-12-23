class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.first = None
        self.last = None

    def treeToDoublyList(self, root):
        # 2 ways to do this. I just don't like using vars outside stack
        def _recurse(node):
            #nonlocal last, first
            if node:
                _recurse(node.left)
                if self.last:
                    self.last.right = node
                    node.left = self.last
                else:
                    self.first = node        
                self.last = node
                _recurse(node.right)
        if not root:
            return None
        
        #first, last = None, None
        _recurse(root)
        self.last.right = self.first
        self.first.left = self.last
        #return self.first


if __name__ == "__main__":
    t = Node(4)
    t.left = Node(2)
    t.right = Node(5)
    t.left.left = Node(1)
    t.left.right = Node(3)
    dll = Solution()
    dll.treeToDoublyList(t)
    print(dll.first.left.val, dll.first.val, dll.first.right.val)
