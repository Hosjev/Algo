"""
You're given an array of ints where each int represents a jump of its value in the array.
For instance, int 2 represents a jump of 2 indices forward in the array; the int -3 is
a jump of 3 indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance,
a jump of -1 at index 0 takes you to -1 in the array. Also, a jump of 1 at the last index 
takes you to 0.

Write a function that returns a boolean representing whether the jumps in the array form a 
single cycle. A single cycle occurs if, starting at any index in the array and following
the jumps, every element in the array is visited exactly once before landing back on the starting
index.

Input:
    array = [2, 3, 1, -4, -4, 2]
Output:
    True

* clarity - this means, starting at index 0, each number moves ONCE
            and each INDEX is visited ONCE and finally returns to 0
* if new position never passes starting point 0
  if number of moves is never greater than length of array, fail?
answer - O(N)T O(1)S
"""

def single_cycle(array):
    # 3 possible outcomes?
    # 1-start at 0, end at 0, visit all
    #   the while loop and count at indices ensure we exit before count crosses
    # 2-start at 0, end at not-0, visit all (or not)
    #   the pos == end ensures we return the start as the end (full circle)
    # 3-start at 0, end at 0, visit not all
    #   the count > 0 with completing cycle means we have more than 1 cycle
    count = 0
    pos = 0
    end = 0

    while count < len(array):
        # If we're still inside the loop and we cross the start
        if count > 0 and pos == end:
            return False
        pos = next_position(array, pos)
        print("current pos/count:", pos, count)
        count += 1

    return pos == end

def next_position(arr, idx):
    step = arr[idx]
    new_position = (idx + step) % len(arr)
    return new_position


def hasSingleCycle(array):
    # This version follows the steps in the array

    visited = [False] * len(array)
    starting_position = 0
    max_jumps = starting_position

    for idx in range(len(array)):
        max_jumps = max(max_jumps, idx + array[idx])
        new_position = (idx + array[idx]) % len(array)
        if visited[new_position]:
            return False
        else:
            visited[new_position] = True

    return True if max_jumps >= len(array) else False


def next_idx(cI, array):
    steps = array[cI]
    nI = (cI + steps) % len(array)
    return nI
    #return nI if nI >= 0 else nI + len(array)


def hasSingleCycle(array):
    # This version follows the loop with a counter
    counter = 0
    current_idx = 0

    # The final element visited will be 1+ len of array
    while counter < len(array):
        # If we ever return to the starting index while inside the loop
        if counter > 0 and current_idx == 0:
            return False
        counter += 1
        current_idx = next_idx(current_idx, array)

    return current_idx == 0



if __name__ == "__main__":

    array = [2, 3, 1, -4, -4, 2]
    #array = [2, 3, 1, -3, -4, 2]
    array = [1, -1, 1, -1]
    array = [1, 1, 0, 1, 1] # F
    array = [0, 1, 1]
    array = [2, 3, 1, -4, -4, 2]

    print(hasSingleCycle(array))
    print(single_cycle(array))
