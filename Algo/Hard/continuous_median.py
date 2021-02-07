"""
Write a ContMedianHandler.
    -continuous insertion of numbers with the insert method.
    -the instant O(1) time retrieval of the median of the numbers that have been inserted thus far w/getMedian method.

The getMedian method has already been written for you.

The median of a set of numbers is the "middle" number WHEN the numbers are ordered from smallest to largest. If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle (3 prior); if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the 2 middle numbers ( (3+7) / 2 == 5 ).

Input:
    ContinuousMedianHandler()

Output:
    insert(5): -
    insert(10): -
    getMedian(): 7.5
    insert(100): -
    getMedian(): 10

answer - O(WS + NM 8^S)T -- W=words in our trie; N/M is our 2D matrix and the most 8 times S levels we recursively search
       - O(WS + NM)S
"""
import time

class Heap:
    def __init__(self, array, heap_type):
        # Do not edit the line below.
        self.heap = array
        self.heap_type = heap_type

    def _swap(self, a, b, array):
        # Just feed the index
        val1 = array[a]
        val2 = array[b]
        array[a] = val2
        array[b] = val1
        return array

    def siftDown(self, p_idx, last, array):
        # Adapt this for either max/min
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
                if self.heap_type == "max": swap_idx = left
                else: swap_idx = right
            else:
                if self.heap_type == "max": swap_idx = right
                else: swap_idx = left

            # Which, if any, node to swap. And advance.
            if (array[p_idx] < array[swap_idx]) and (self.heap_type == "max") or \
               (array[p_idx] > array[swap_idx]) and (self.heap_type == "min"):
                array = self._swap(p_idx, swap_idx, array)
                p_idx = swap_idx
                left = (p_idx * 2) + 1
            else:
                return

    def siftUp(self, current_idx, array):
        p_idx = (current_idx - 1) // 2
        while p_idx >= 0:
            if (array[p_idx] > array[current_idx] and self.heap_type == "min") or \
               (array[p_idx] < array[current_idx] and self.heap_type == "max"):
                array = self._swap(p_idx, current_idx, array)
                current_idx = p_idx
                p_idx = (current_idx - 1) // 2
            else:
                break

    def remove(self):
        root = self.heap[0]
        array = self._swap(0, len(self.heap) - 1, self.heap)
        array.pop()
        self.siftDown(0, len(array) - 1, array)
        return root

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)



class ContinuousMedianHandler:
    # This is about using heaps (min/max)
    def __init__(self):
        self.median = None
        # Four data structures to track
        self.ints = []
        self.medians = []
        self.lower = Heap([], "max")
        self.higher = Heap([], "min")

    def insert(self, number):
        self.ints.append(number)
        self.eval_heaps(number)
        self.setMedian()

    def setMedian(self):
        # At this point, the heaps should be balanced
        if len(self.lower.heap) == len(self.higher.heap):
            med = (self.lower.heap[0] + self.higher.heap[0]) / 2
            self.medians.append(med)
        else:
            if len(self.lower.heap) > len(self.higher.heap):
                self.medians.append(self.lower.heap[0])
            else:
                self.medians.append(self.higher.heap[0])
        self.median = self.medians[-1]

    def eval_heaps(self, number):
        # Abstracting this b/c of the # of edge cases
        low = len(self.lower.heap)
        high = len(self.higher.heap)

        # Are heaps currently empty?
        if low == 0 and high == 0:
            self.lower.insert(number)
        elif number < self.lower.heap[0]:
            self.lower.insert(number)
        else:
            self.higher.insert(number)

        # Balance if necessary
        low = len(self.lower.heap)
        high = len(self.higher.heap)
        if abs(low - high) == 2:
            if low > high:
                num = self.lower.remove()
                self.higher.insert(num)
            else:
                num = self.higher.remove()
                self.lower.insert(num)

    def getMedian(self):
        return self.median




if __name__ == "__main__":


    cm = ContinuousMedianHandler()

    cm.insert(5)
    cm.insert(10)
    cm.insert(100)
    cm.insert(200)
    cm.insert(6)
    cm.insert(13)
    cm.insert(14)
    print(cm.getMedian())
