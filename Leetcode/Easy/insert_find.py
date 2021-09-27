def insert_or_find(nums, target):
    """
    1. given a sorted array, find target or index
       (prior+) where it would be inserted
    2. classic binary search
       a. keep dividing array in half till you
          get a present or not
       b. bin search works on sorted only w/<>
    """
    return binary_helper(0, len(nums) - 1, nums, target)


def binary_helper(S, E, nums, target):
    """
    This helper follows indices

    Arguments:
        S = int (starting index within array)
        E = int (ending index within array)
        nums = array
        target = int (number to look for)

    ** equation = (E - S) // 2 = len of stretch
    """    

    # Our exit or 1st return up the stack should we reach last
    if (S == E):
        # If at end AND target is greater than last index int
        if (S == len(nums) - 1) and (target > nums[S]):
            return S + 1
        # Our target equals OR is less than integer
        else:
            return S

    middle = (E - S) // 2
    left = (S, S+middle)
    right = (S+middle+1, E)

    # Target reached, immediate return
    if target == nums[left[1]]:
        return left[1]
    if target == nums[right[0]]:
        return right[0]

    # Left
    if target < nums[left[1]]:
        answer = binary_helper(left[0], left[1], nums, target)
    # Right
    else:
        answer = binary_helper(right[0], right[1], nums, target)

    return answer




a = [0, 1, 2, 3, 4, 5, 6, 7] # indices
a = [1, 2, 3, 4, 5, 6, 7, 8]
a = [1, 2, 3, 5, 6, 7, 9, 10, 11]
t = 8
a = [1]
t = 0
a = [1, 2, 3]
t = 0
print(insert_or_find(a, t))

# 1st problem -- end of array
print(insert_or_find([1, 3, 5, 6], 7))
print(insert_or_find([1, 3, 5, 8], 7))
