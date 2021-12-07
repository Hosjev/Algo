from typing import List
from collections import defaultdict
from queue import Queue


class Node:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.cache = defaultdict(list)

    def _traverse(self, level, node):
        q = Queue()
        q.put((level, node))
        while not q.empty():
            key, item = q.get()
            self.cache[key].append(item.val)
            if item.left:
                q.put((key - 1, item.left))
            if item.right:
                q.put((key + 1, item.right))

    def verticalOrder(self, root) -> List[List[int]]:
        if not root: return []
        self._traverse(0, root)
        # Sort our cache by key, then return nested lists
        return [self.cache[k] for k in sorted(self.cache)]



if __name__ == "__main__":
    t = Node(4)
    t.left = Node(2)
    t.right = Node(5)
    t.left.left = Node(1)
    t.left.right = Node(3)
    obj = Solution()
    print(obj.verticalOrder(t))
