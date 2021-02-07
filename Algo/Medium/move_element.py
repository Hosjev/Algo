"""
Write function that takes array of ints and an int to move. Move the int to the end of the
array in place.
Input:
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    elem = 2
Output:
    [4,1,3,2,2,2,2,2]

* create two pointers on each end and move them respectively, only advancing on conditions
   then quit when met in the middle as all indices have been processed
answer - O(N)T / O(1)S
"""
import time

def moveElementToEnd(array, element):

    def swap (a, b):
        return b, a

    # Pointers are num and end
    # NUM moves right, END moves left
    # the middle gets fuzzy. I still need to process the middle, but how w/o going
    #  out of bounds on the R pointer? Do NOT go past the mid on R pointer.
    left = 0
    right = len(array)-1

    while left < right:
        print(f"...left/right: {left,right}")
        #time.sleep(.3)
        # If left is element, look for viable right
        if array[left] == element:
            while array[right] == element:
                right -= 1
                if right < (len(array) // 2): break
            print(f"...swapping l/r: {left,right}")
            array[left], array[right] = swap(array[left], array[right])
            left += 1
            right -= 1
        else:
            if left > (len(array) // 2): break
            left += 1

    return array
        



if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    elem = 2
    array = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
    elem = 5

    print(moveElementToEnd(array, elem))
