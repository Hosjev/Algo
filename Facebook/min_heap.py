class Solution:
    def __init__(self, array):
        self.heap = array
        self.empty = len(self.heap) == 0
        self.build_heap()

    def build_heap(self):
        if self.empty: return
        start = 0
        end = (len(self.heap) - 2) // 2
        for i in reversed(range(start, end + 1)):
            self._sift_down(i)

    def _sift_down(self, p_idx):
        stop = len(self.heap) - 1
        left = (p_idx * 2) + 1
        while left <= stop:
            right = (p_idx * 2) + 2
            if right == len(self.heap):
                right = None
            # Eval local
            if right and self.heap[right] < self.heap[left]:
                swap_idx = right
            else:
                swap_idx = left
            # Swap if necessary
            if self.heap[p_idx] > self.heap[swap_idx]:
                self._swap(p_idx, swap_idx)
                p_idx = swap_idx
                left = (p_idx * 2) + 1
            else:
                return

    def _sift_up(self, i):
        p_idx = (i - 1) // 2
        while p_idx >= 0:
            if self.heap[p_idx] > self.heap[i]:
                self._swap(p_idx, i)
                i = p_idx
                p_idx = (i - 1) // 2
            else:
                break

    def remove_root(self):
        if self.empty: return
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        self._sift_down(0)

    def insert(self, n):
        self.heap.append(n)
        self._sift_up(len(self.heap) - 1)

    def _swap(self, p, s):
        self.heap[p], self.heap[s] = self.heap[s], self.heap[p]


a = [43, 5, 10, 18, 2, 23, 30, 12]
#a = []
s = Solution(a)
# General case - rem int min
# EC - rem empty root
#s.remove_root()
s.insert(1)
print(s.heap)
