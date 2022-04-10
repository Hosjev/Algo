"""
Write function that takes array of ints and returns a sorted version. Using the insertion algorithm.
Input:
    array = [8, 5, 2, 9, 5, 7, 3] 0
    array = [5, 8, 2, 9, 5, 6, 3]
    array = [5, 2, 8, 9, 5, 6, 3] 1
    array = [2, 5, 8, 9, 5, 6, 3] 1
    array = [2, 5, 8, 9, 5, 6, 3] 2
    array = [2, 5, 8, 5, 9, 6, 3] 3
    array = [2, 5, 5, 8, 9, 6, 3] 3
    array = [2, 5, 5, 8, 9, 6, 3] 4
    array = [2, 5, 5, 8, 6, 9, 3] 4
    array = [2, 5, 5, 6, 8, 9, 3] 4
    array = [2, 5, 5, 6, 8, 9, 3] 5
    array = [2, 5, 5, 6, 3, 8, 9] 5
    array = [2, 5, 5, 3, 6, 8, 9] 5
    array = [2, 3, 5, 5, 6, 8, 9] 5
Output:
    [2, 3, 5, 5, 6, 8, 9]

* Insertion algorithm:
  1-compare 1st 2 ints
  3-compare last int to previous, if smaller, move left
  4-do this until exhausted to zero
"""

def insertionSort(array):
    # Steps:
    # For loop, compare 2 to 1
    # if 2 less than 1, swap
    # compare 3 to 2
    # if 3 less than 2, swap
    #  go backward, if 2 less than 1, swap
    # so this algo grows as we go, going backward to 0 at end IF SWAPPED
    def swap(one, two):
        return two, one   

    for idx in range(len(array)-1):
        if array[idx] > array[idx+1]:
            array[idx], array[idx+1] = swap(array[idx], array[idx+1])
            # Work your way backward here
            for r_idx in range(idx, 0, -1):
                if array[r_idx] < array[r_idx-1]:
                    array[r_idx], array[r_idx-1] = swap(array[r_idx], array[r_idx-1])
    return array



if __name__ == "__main__":
    # Steps:
    array = [8, 5, 2, 9, 5, 6, 3]
    print(insertionSort(array))
