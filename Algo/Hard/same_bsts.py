"""
Write a function that compares two arrays to determine if, given the order and length of the array, if they can write out the same BinarySearchTree. All nodes to left less-than, all nodes to right greater-than or equal-to.

Input:
    array_a = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array_b = [10, 8, 5, 15, 2, 12, 11, 94, 81]

Output:
    True

answer - O(N)T / O(N)S
"""

def sameBsts(arrayOne, arrayTwo):
    # Call recursion
    # Our final return up the stack to each side of the single caller
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    if len(arrayOne) != len(arrayTwo):
        return False

    # Process one
    node_A = arrayOne.pop(0)
    left_arr_A = [x for x in arrayOne if x < node_A]
    right_arr_A = [x for x in arrayOne if x >= node_A]

    # Process two
    node_B = arrayTwo.pop(0)
    left_arr_B = [x for x in arrayTwo if x < node_B]
    right_arr_B = [x for x in arrayTwo if x >= node_B]

    return sameBsts(left_arr_A, left_arr_B) and sameBsts(right_arr_A, right_arr_B)




if __name__ == "__main__":

    array_a = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    array_b = [10, 8, 5, 15, 2, 12, 11, 94, 81]

    #array_a = [10, 15, 8, 12, 94, 81, 5, 2, -1, 100, 45, 12, 9, -1, 8, 2, -34]
    #array_b = [10, 8, 5, 15, 2, 12, 94, 81, -1, -1, -34, 8, 2, 9, 12, 45, 100]

    array_a = [10, 15, 8, 12, 94, 81, 5, 2, 10]
    array_b = [10, 8, 5, 15, 2, 10, 12, 94, 81]

    print(sameBsts(array_a, array_b))
