"""
Write function takes in a non-empty array of ints and returns array of same length where output is equal to product of every other input. Output[i] is equal to all input[*] except input[i]. Solve prob w/o using division.

Input:
    input = [5, 1, 4, 2]
Output:
    [8, 40, 10, 20]
    8 = 1x4x2
    40 = 5x4x2
    10 = 5x2x1
    20 = 5x4x1


"""
import time


def arrayOfProducts(array):
    # Write your code here.
    # the naive approach is multiplying all others
    # using array slices
    # we can mitigate time by forwarding past solutions
    # prev * [i-1] * arr[i:]

    output = [None] * len(array)
    marker = 0
    previous_sum = 1

    while (marker < len(array)):
        m_sum = 1
        for x in array[marker+1:]:
            m_sum *= x
        if marker == 0:
            output[marker] = previous_sum * m_sum
            previous_marker = 1
        else:
            output[marker] = previous_sum * \
                array[marker-1] * m_sum
            previous_marker = array[marker-1]
        previous_sum = previous_sum * previous_marker
        marker += 1

    return output


array = [5, 1, 4, 2]
print(arrayOfProducts(array))
