class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Ruleset:
    1) get
        a) in hash
            1) return node value
            2) remove from DLL
            3) insert as head
        b) not in hash
            1) return -1
    2) put
        a) in hash
            1) remove node
            2) fix pointers (both DLL/hash)
            3) insert as head
            4) fix pointers (both DLL/hash)
            5) update w/new value
        b) not in hash
            1) LRU not at capacity?
                a) create node
                b) add to hash
                c) insert at head
            2) LRU at capacity?
                a) grab tail
                b) fix pointers (both DLL/hash)
                c) create node
                d) add to hash
                e) insert at head
    TODO: turn "get" into asynchronous method
          ie--return -1 or value immediately
    """

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0) # dummy head
        self.tail = ListNode(-1, -1) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


lru = LRUCache(2)
lru.put(1, 1)
print(lru.dic)
print(lru.dic[1].value)
print(lru.head.next.value)
print(lru.tail.prev.value)
lru.put(2, 2)
print(lru.dic)
print(lru.dic[1].value)
print(lru.head.next.value)
print(lru.tail.prev.value)
lru.get(1)
print(lru.dic)
print(lru.dic[1].value)
print(lru.head.next.value)
print(lru.tail.prev.value)
lru.put(3, 3)
print(lru.dic)
print(lru.dic[1].value)
print(lru.head.next.value)
print(lru.tail.prev.value)
lru.get(2)
print(lru.dic)
lru.put(4, 4)
print(lru.dic)
print(lru.head.next.value)
print(lru.tail.prev.value)
lru.get(1)
lru.get(3)
lru.get(4)
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]

