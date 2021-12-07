class Node:
    """ Doubly Linked List Object """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache: 
  
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(float("inf"), "head")
        self.tail = Node(float("-inf"), "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        return
  
    def get(self, x):
        try:
            node = self.cache[x]
            self._remove_node(node)
            self._insert_head(node)
            return node.value      
        except KeyError:
            return -1

    def set(self, x, y):
        # Write your code here
        node = None
        if x in self.cache:
            node = self.cache[x]
            node.value = y
            self._remove_node(node)
        else:
            if self.capacity == len(self.cache):
                self._remove_tail()
            node = Node(x, y)
            self.cache[x] = node
        self._insert_head(node)    

    def _insert_head(self, node):
        next = self.head.next
        self.head.next = node
        next.prev = node
        node.prev = self.head
        node.next = next
      
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
      
    def _remove_tail(self):
        if len(self.cache) == 0: return
        tail = self.tail.prev
        prev = tail.prev
        prev.next = self.tail
        self.tail.prev = prev
        del self.cache[tail.key]


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.set(1,2)
    lru.set(2,3)
    print(lru.head.next.key)
    lru.set(1,5)
    print(lru.head.next.key)
    lru.set(4,5)
    lru.set(6,7)
    print(lru.get(4))
    lru.set(1,2)
    print(lru.get(3))
