"""
Write function that takes sorted array of ints as well as target int. Function should use
binary search algorithm to determine if target int is contained in the array and return
its index #. If not contained, return -1.
Input:
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
Output:
    3 (index)

* watch binary search algo
* BINARY SEARCH algo works on SORTED elements
[3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6]

[0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
...inner positions-l/r/m: (0, 9, 4)
...pos LP/RP/MP: (0, 4, 2)
[0, 1, 21, 33]
...inner positions-l/r/m: (0, 4, 2)
...pos LP/RP/MP: (2, 4, 3)
[21, 33]
...inner positions-l/r/m: (2, 4, 3)
hello
[]


"""
import time

def binarySearch(array, target):
    # RETURN POSITIONS!!!
    
    def inner_bs(left, right, middle_position):
        #print(f"...inner positions-l/r/m: {LP, RP, MP}")
        #time.sleep(1)
        if array[middle_position] == target:
            return middle_position
        if left == right == middle_position:
            return -1

        if array[middle_position] < target:
            left = middle_position+1
        elif array[middle_position] > target:
            right = middle_position-1

        middle_position = (left+right) // 2
        #print(f"...pos LP/RP/MP: {LP,RP,MP}")
        return inner_bs(left, right, middle_position)

    return inner_bs(0, len(array)-1, (0+len(array)-1) // 2)




if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 61

    print(binarySearch(array, target))
