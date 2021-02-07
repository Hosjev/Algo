"""
Sort an array using the heap sort method.

Input:
    array = [8, 5, 2, 9, 5, 6, 3]

Output:
    5

answer - O(N^2)T / O(N)S
"""
import time

class MaxHeap:
    def __init__(self, array):
        self.build_heap(array)

    def _swap(self, a, b, array):
        # Just feed the index
        val1 = array[a]
        val2 = array[b]
        array[a] = val2
        array[b] = val1
        return array

    def build_heap(self, array):
        start_idx = (len(array) - 2) // 2
        end_idx = len(array) - 1
        for x in reversed(range(start_idx + 1)):
            self.sift_down(x, end_idx, array)

    def sift_down(self, p_idx, end_idx, array):
        # (i * 2) + 1 (left) or 2 (right)
        left = (p_idx * 2) + 1
        # last one, p=0, l=1, e=1
        while left <= end_idx:
            # Edge case for end of array (even length)
            if (p_idx * 2) + 2 <= end_idx:
                right = (p_idx * 2) + 2
            # I don't know if this is properly handling of this case
            # but when there is no official "right", I'm mocking a right
            # by making it the same as left. I can't see the harm.
            else:
                right = end_idx

            #print(p_idx, end_idx, left, right, array)
            #time.sleep(.2)
            # Which child node to attempt to swap
            if (array[right] < array[left]):
                swap_idx = left
            else:
                swap_idx = right

            # Which, if any, node to swap. And advance.
            if array[p_idx] < array[swap_idx]:
                array = self._swap(p_idx, swap_idx, array)
                p_idx = swap_idx
                left = (p_idx * 2) + 1
            else:
                return


def heapSort(arr):
    """
    Within recursive method.
    1-turn array into maxHeap
    2-swap 0 with end of array
    3-sift 0 down to end-1
    4-recur on new arr heap 0-->swapped idx
    """
    mh = MaxHeap(arr)
    #print(arr)
    recur_heapsort(mh, arr, 0, len(arr) - 1)
    return arr


def recur_heapsort(mh, arr, start_idx, end_idx):
    # We're only returning when arr is empty
    # mh.heap = array
    # This takes us completely out. Arr length 1 or smaller.
    if end_idx == 0:
        return

    #print(start_idx, end_idx, arr)
    _swap(start_idx, end_idx, arr)
    mh.sift_down(start_idx, end_idx - 1, arr)
    recur_heapsort(mh, arr, start_idx, end_idx - 1)


def _swap(l, r, arr):
    arr[l], arr[r] = arr[r], arr[l]
    



if __name__ == "__main__":

    array = [8, 5, 2, 9, 7, 6, 3]
    #array = [1, 2, 3]
    #array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
    array = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
    array = [ 8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4 ]
    array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
    array = [ 2, -2, -6, -10, 10, 4, -8, -1, -8, -4, 7, -4, 0, 9, -9, 0, -9, -9, 8, 1, -4, 4, 8, 5, 1, 5, 0, 0, 2, -10 ]
    array = [ 4, 1, 5, 0, -9, -3, -3, 9, 3, -4, -9, 8, 1, -3, -7, -4, -9, -1, -7, -2, -7, 4 ]

    print(heapSort(array))
