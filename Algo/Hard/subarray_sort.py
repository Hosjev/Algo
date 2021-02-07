"""
Write a function that, given an array of probably unsorted ints, returns a two-digit list representing the starting and ending point at which the array would Have to be sorted. A subarray of indices.

Input:
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

Output:
    [3, 9] 

answer - O(N)T / O(1)S
"""

def subarraySort(arr):
    # Skip logic if array already sorted
    if sorted(arr) == arr: return [-1, -1]

    sub_positions = [None, None]
    max_value = arr[0]

    for idx in range(1, len(arr)):
        # Eval max
        if arr[idx] >= max_value:
            max_value = arr[idx]
            #print(f"On {idx} new max set: {max_value}")
        else:
            if sub_positions[0] is None:
                # We have a decrement and the beginning of our subarray
                # Reverse search for less than
                sub_positions[0] = reverse_search(arr, idx, idx - 1)
                #print(f"First sub pos set: {sub_positions}")
            # 
            elif arr[sub_positions[0]] > arr[idx]:
                sub_positions[0] = reverse_search(arr, idx, sub_positions[0])
            sub_positions[1] = idx

    return sub_positions

def reverse_search(arr, current_idx, new_idx):
    # Return the position that qualifies as new low
    while new_idx > -1:
        if arr[current_idx] >= arr[new_idx]:
            return new_idx + 1
        else:
            new_idx -= 1

    # As a failsafe, return index 0
    return 0




if __name__ == "__main__":
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # returns 3, 9
    #array = [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]
    # returns 4, 9
    #array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19, -1]
    array = [1, 2, 8, 4, 5]
    #array = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]
    # 11, 12 --wrong, should be 0 to end

    print(subarraySort(array))
