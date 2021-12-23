class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node("head")
        self.length = 0

    def length(self):
        return self.length

    def insert(self, data):
        obj = Node(data)
        obj.next = self.head.next
        self.head.next = obj
        self.length += 1

    def append(self, data):
        pointer = self.head
        obj = Node(data)
        while pointer.next:
            pointer = pointer.next
        pointer.next = obj
        self.length += 1

    def find(self, data):
        if not self.length: return
        pointer = self.head.next
        while pointer:
            if pointer.value == data:
                return data
            pointer = pointer.next
        return pointer

    def delete(self, data):
        if not self.length: return
        pointer = self.head
        while pointer.next:
            if pointer.next.value == data:
                break
        if not pointer.next: return
        pointer.next = pointer.next.next
        self.length -= 1
        return data

    def print(self):
        return self._print(self.head.next)

    def _print(self, node):
        if not node: return
        print(node.value)
        return self._print(node.next)


#def main():
    #l_obj = LinkedList()
    #l_obj.insert(1)
    #l_obj.print()
    #l_obj.delete(1)
    #l_obj.print()
    #l_obj.insert(1)
    #l_obj.append(2)
    #l_obj.append(3)
    #l_obj.print()
    #print(l_obj.find(4))
    #print(l_obj.length)


#main()
