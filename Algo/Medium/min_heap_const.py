"""
Implement a a MinHeap class that supports:
    Building a min heap from an input array of ints
    Inserting ints into the heap
    Removing the heap's minimum / root value
    Peeking at the heap's minimum / root value
    Sifting ints up and down the heap, which is to be used when inserting and removing

Note that the heap should be represented in the form of an array.

Input:
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

Output:
    MinHeap(array) - instantiating calls method below
    buildHeap(array): [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
    insert(76) (end)
    peak(): -5
    remove(): -5
    peak(): 2
    remove(): 2
    peak(): 6
    insert(87) (end)

* a min heap is a binary tree with 2 additional properties:
      1-it must be complete, ie--every level filled out except the last which can be
        partial but occupied from LEFT to RIGHT
* a MIN heap is distinguished from a MAX heap by: 
      nodes are LESS THAN children nodes (with no sorting thereafter)
             8
           /   \
         12    23
         / \   / \
       17  31 30  44
       / \           
    108  19

O(d)T - depth | O(1)S
"""

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peak, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array, heapType):
        # Do not edit the line below.
        self.heap = self.buildHeap(array, heapType)

    def _swap(self, a, b, array):
        # Just feed the index
        val1 = array[a]
        val2 = array[b]
        array[a] = val2
        array[b] = val1
        return array

    def buildHeap(self, array, heapType):
        # BH is essentially satisfying the completeness of a heap
        # Notice this is done on an UNSORTED array
        # Say on a 9 len array, 3 would start, 8 would mark the end
        # 3 IS THE LAST PARENT W/CHILDREN
        start_pos = (len(array) -2)  // 2
        end_pos = len(array) - 1
        # Loop through every parent node, sifting down until to zero
        # Say on that 9 len array, this would read 3,2,1,0 and feed 8
        for p_idx in reversed(range(start_pos + 1)):
            self.siftDown(p_idx, end_pos, array, heapType)

        return array

    def siftDown(self, p_idx, last, array, heapType):
        # Write your code here.
        # (i * 2) + 1 (left) or 2 (right)
        left = (p_idx * 2) + 1
        while left <= last:
            # Edge case for end of array (even length)
            if (p_idx * 2) + 2 <= last:
                right = (p_idx * 2) + 2
            else:
                right = -1 

            # Which child node to attempt to swap
            if (right != -1) and (array[right] < array[left]):
                if heapType == "max": swap_idx = left
                else: swap_idx = right
            else:
                if heapType == "max": swap_idx = right
                else: swap_idx = left

            # Which, if any, node to swap. And advance.
            if (array[p_idx] < array[swap_idx] and heapType == "max") or \
               (array[p_idx] > array[swap_idx] and heapType == "min"):
                array = self._swap(p_idx, swap_idx, array)
                p_idx = swap_idx
                left = (p_idx * 2) + 1
            else:
                return


    def siftUp(self, current_idx, array, heapType):
        # Write your code here.
        p_idx = (current_idx - 1) // 2
        while p_idx >= 0:
            if (array[p_idx] > array[current_idx] and heapType == "min") or \
               (array[p_idx] < array[current_idx] and heapType == "max"):
                array = self._swap(p_idx, current_idx, array)
                current_idx = p_idx
                p_idx = (current_idx - 1) // 2
            else:
                break
        return

    def peek(self):
        # Write your code here.
        # This is our "peak" not peek
        return self.heap[0]

    def remove(self, heapType):
        # Write your code here.
        # Notice this has no variable or argument for choice.
        # It's always root
        root = self.heap[0]
        array = self._swap(0, len(self.heap) - 1, self.heap)
        array.pop()
        self.siftDown(0, len(array) - 1, array, heapType)
        return root

    def insert(self, value, heapType):
        # Write your code here.
        # We insert at the end of self.heap then run siftUp
        # Insert then siftUp
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap, heapType)




if __name__ == "__main__":

    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

    m = MinHeap(array, "min")
    print(m.heap)
    m.insert(10, "min")
    print(m.heap)
    print(m.remove("min"))
    print(m.heap)
    print(m.peek())

    mx = MinHeap(array, "max")
    print(mx.heap)
    mx.insert(10, "max")
    print(mx.heap)
    print(mx.remove("max"))
    print(mx.heap)
    print(mx.peek())
