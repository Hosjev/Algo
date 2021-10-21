class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
    Questions:
    1) What is amount of data we want to cache?
       TBs
    2) What is type of data? String takes less, images more.
       TBs / (Amount of memory per (nodes/machines)) * 2 to double.
       Prod mach = 72GB with 30TB per second? 30240 / 72 = 420 : Tera to Gig 1024T to 1G
    3) Which eviction strategy is appropriate?
       FIFO works well natively with queues is fast, but access times could suffer
       LRU has a read constant time (could be improved with async DB write)
       LFU has a read constant time but takes more computing power to track timestamps
    4) What access pattern should it follow?
       Write through - success == writes to cache then DB, slower response
       Write around  - writes to DB then cache retrieves, slower response
       Write back    - writes to cache then async writes to DB, high response but requires redundancy
    5) Number of queries per second and type of data?
       10Mi QPS
    6) Issues to address: 1-Latency, 3-Consistency, 2-Availability
    7) Shard method/strategy? At the memory level.
    8) Collision prevention/locking strategy? At the hash level. READS must be Queen.
       suggestion: allow locking (esp when multi-threaded) on individual hash entry level
                   this would require storing not just single value "key" entries but
                   priming the key as a Linked List so h[k] = LL of value
                   (though the above was suggested a much fuller data structure)
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.h_cache = dict()
        # Dummy head/tail == fewer ops
        self.head = ListNode(float("inf"), 0)
        self.tail = ListNode(float("-inf"), -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        try:
            node = self.h_cache[key]
            self.removeNode(node)
            self.insertHead(node)
            return node.value
        except KeyError:
            return -1


    def put(self, key, value):
        node = None
        if key in self.h_cache:
            node = self.h_cache[key]
            node.value = value
            self.removeNode(node)
        else:
            node = ListNode(key, value)
            if len(self.h_cache) >= self.capacity:
                self.removeTail()
            self.h_cache[key] = node
        self.insertHead(node)


    def removeTail(self):
        # ... 1 <-> 2 <-> T
        if len(self.h_cache) == 0:
            return
        tail = self.tail.prev
        prev = tail.prev
        prev.next = self.tail
        self.tail.prev = prev
        # Last op, scrub hash
        del self.h_cache[tail.key]
        

    def insertHead(self, node):
        # <- H <-> T ->
        # <- H <-> (1) <-> T ->
        next = self.head.next
        self.head.next = node
        node.next = next
        next.prev = node
        node.prev = self.head


    def removeNode(self, node):
        # ... 2 <-> 3 <-> 4 ...
        node.prev.next = node.next
        node.next.prev = node.prev


lru = LRUCache(2)
lru.put(1, 1)
print(lru.head.next.value)
lru.put(2, 2)
print(lru.head.next.value)
lru.get(1)
print(lru.head.next.value)
lru.put(3, 3)
print(lru.head.next.value)
print(lru.h_cache)
lru.get(3)
print(lru.head.next.value)
lru.put(4, 4)
print(lru.head.next.value)
