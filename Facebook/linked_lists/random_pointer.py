from typing import Optional
from collections import defaultdict


class Node:
    def __init__(self, x: int):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    def _recur_on_node(self, node, cache):
        # Run this as a DFS
        if not node:
            return None
        if not node in cache:
            clone = Node(node.val)
            cache[node] = clone
            clone.next = self._recur_on_node(node.next, cache)
            clone.random = self._recur_on_node(node.random, cache)
            return clone
        else:
            return cache[node]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Edge Case(s)
        if not head: return head

        # Logic - use cache as visited list
        cache = defaultdict(Node)
        self._recur_on_node(head, cache)
        return cache[head]



if __name__ == "__main__":
    linked = Node(7)
    linked.next = Node(13)
    linked.next.next = Node(11)
    linked.next.next.next = Node(10)
    linked.next.next.next.next = Node(1)
    # 13
    linked.next.random = linked
    # 11
    linked.next.next.random = linked.next.next.next.next
    # 10
    linked.next.next.next.random = linked.next.next
    # 1
    linked.next.next.next.next.random = linked
    obj = Solution()
    cloned = obj.copyRandomList(linked)
