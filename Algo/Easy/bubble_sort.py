"""
Write function that takes in array of ints and returns sorted version of that array.
Use bubble sort algorithm to sort the array.
Input:
    array = [8, 5, 2, 9, 5, 6, 3]
Output:
    [2, 3, 5, 5, 6, 8, 9]

* bubble sort algo: iterate thru array multiple times
  1st time: iterate thru ALL, swapping 1 and 2 for max to the Right
  check for "changes" inside rhythm. if so, perform iteration again
  on each iteration, the LAST number is guaranteed to be largest,
    so our array iteration will be MINUS 1
"""

def bubbleSort(array):
    # Steps:
    # 1-iterate
    # 2-keep track of IF SWAPPED (bool)
    # 3-if swapped, decrease array traverse by -1
    # 4-if not swapped, return array (THIS IS OUR FINAL RETURN)

    return sorter(array, False)


def swap(one, two):
    return two, one


def sorter(arr, final):
    if final:
        return array
    final = True
    # Start from front
    for idx in range(len(arr)-1):
        # if current is greater than next
        print(f"...in memory, {idx} is {arr[idx]}")
        if array[idx] > array[idx+1]:
            final = False
            array[idx], array[idx+1] = swap(array[idx], array[idx+1])
    # Put whole array thru the machine
    return sorter(arr[0:len(arr)-1], final)



if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    print(array)
    print(bubbleSort(array))

