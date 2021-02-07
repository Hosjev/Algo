"""
Write function that takes a special array and returns its product sums.
Input:
    [5, 2, [7, -1], 3, [6, [-13, 8], 4] ]
    Level 1
Output:
    12
    # 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
              L2 *              L2*      L3*

* a special array is a non-empty array that contains either ints or other spec arrays
* the product sum of a special array is the sum of its elements, where spec arrays inside it
    are also summed then multiplied by their level of depth
* the depth of a special array is how far nested it is.
    ex: [] is 1
        [ [] ] is 2
        [ [ [] ] ] is 3
  therefore product sum of [ x, y ] is x + y
            product sum of [ x, [y, z] ] is x + 2 * (y + z)
            product sum of [ x, [y, [z] ] ]
"""
import time

def productSum(array):
    # 1 way: make new array and add to it after resolving special arrays then sum array
    # 2 way: iterate and recursively incr/dcr levels, finally summing

    def inner_sum(array, l):

        total = 0
        # The total is overwritten for each list
        # ater the inner array, it returns to previous array
        print(f"...total outside loop: {total}")
        for item in array: # each for loop is a level
            print(f"...processing item loop: {item}")
            if isinstance(item, list):
                total += inner_sum(item, l+1)
            else:
                total += item
        print(f"...outside loop, tot: {total}")
        return total * l

    return inner_sum(array, 1)



if __name__ == "__main__":
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4] ]
    array2 = [5, [7, -1], 2] # 5+12+2=19
    print(productSum(array))
