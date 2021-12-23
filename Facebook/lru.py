class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node("head", "None")
        self.tail = Node("tail", "None")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._make_head(node)
            return node.val
        else:
            return -1

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._remove(node)
        else:
            if len(self.cache) == self.capacity:
                self._pop_tail()
            node = Node(key, val)
            self.cache[key] = node
        self._make_head(node)

    def _pop_tail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.cache[node.key]

    def _remove(self, node):
        # Rem pointers
        node.prev.next = node.next
        node.next.prev = node.prev

    def _make_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node


if __name__ == "__main__":
    lru = LRU(2)
    lru.put(2, 1)
    lru.put(1, 1)
    lru.put(2, 3)
    lru.put(4, 1)
