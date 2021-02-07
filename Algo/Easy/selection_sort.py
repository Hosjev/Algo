"""
Write function that takes array of ints and returns a sorted version. Using the selection algorithm.
Input:
    array = [8, 5, 2, 9, 5, 6, 3]
Output:
    [2, 3, 5, 5, 6, 8, 9]

* selection algorithm:
  1-iterate forward thru list
  2-establish starting point - array zero
  3-compare zero to Every int to insure smallest (keep variable every time < reached)
    swap only as array is exhausted
  4-move onto next int
  5-another interation within iteration
"""

def selectionSort(array):

    def swap(p1, p2):
        return p2, p1

    for run in range(len(array)):
        smallest = array[run] # VALUE in array
        array_position = None
        for idx in range(run+1, len(array)):
            if array[idx] < smallest:
                smallest = array[idx] # reset smallest every time
                array_position = idx
        if array_position:
            array[run], array[array_position] = swap(array[run], array[array_position])

    return array



if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    print(selectionSort(array))
