class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def begin(self, data):
        nNode = Node(data)
        nNode.nextval = self.headval
        self.headval = nNode

    def end(self, data):
        nNode = Node(data)
        node = self.headval
        while node.nextval:
            node = node.nextval
        node.nextval = nNode

    def after(self, after, data):
        nNode = Node(data)
        node = self.headval
        # When you reach the match, set cur to data and data to next
        while node.dataval != after:
            node = node.nextval
        nNode.nextval = node.nextval
        node.nextval = nNode

    def cycle(self):
        def inner_cy(node):
            print(node.dataval)
            if node.nextval: inner_cy(node.nextval)
        inner_cy(self.headval)


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# Insert at top
list1.begin("Sun")

# Insert at end
list1.end("Fri")

# Insert between
list1.after("Wed", "Thu")

list1.cycle()
