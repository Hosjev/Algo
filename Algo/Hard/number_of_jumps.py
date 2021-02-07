"""
You're given an array of positive ints where each int represents the max number of jumps you can take forward in the array.

For ex:
    If element at index 1 is 3, you can go to 2, 3, or 4.

Write a function that returns the minumum number of jumps needed to reach the final index.

Input:
    array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
Output:
    4 # 3 --> 4 or 2; 2 or 3 --> 7 --> 3

* clarity - this means, starting at index 0, each number moves ONCE
            and each INDEX is visited ONCE and finally returns to 0
* if new position never passes starting point 0
  if number of moves is never greater than length of array, fail?
answer - O(N)T O(1)S
"""

def minNumberOfJumps(array):
    """
    In my version, I do this:
        create array of empty positions, null or whatever
        prime the array with first step
        the number of steps stored in [0] in the array forward
        mark my new array with retroactive value of 1 step for that int backward to 1
        [3, 4, 2, 1, ...
        [0, 1, 1, 1, ...
        Now we iterate thru 1-len(a)
        for i in arr:
            i plus index number == new idx
            new_idx in marked array gets current idx val + 1 step
            or possibly a minimum of 2 nums plus 1 step
        *the above solution gets possibly messy when you have [1, 1, 2...]
         you have to start looking backward more than once

    *Algo sol 1:
        orig arr with an arr like mine [ 0, inf, inf,...
        iterate thru orig then steps, looking backward with this formula
            if array[j] + j >= i: jump[i] = min(jumps[i], jump[j+1])

    *Algo sol 2:
        calc maximum reach with steps to take, tracking movements with a variable
    """

    # It takes no steps to reach the end
    if len(array) == 1: return 0

    # Prime the variables
    # The number of steps we have to take to get to current maximum reach
    steps = array[0]
    max_reach = array[0]
    jumps = 0

    for idx in range(1, len(array)):
        if idx == len(array)-1:
            return jumps+1
        max_reach = max(max_reach, (idx + array[idx]))
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - idx # the index I have to reach minus my current position



if __name__ == "__main__":

    array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

    print(minNumberOfJumps(array))
