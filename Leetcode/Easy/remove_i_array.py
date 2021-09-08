def remove_val_array(nums, val):
    """
    1. linear iterate
    2. if i is target val
       a. replace with slicing
    3. same return
    """
    if not nums: return 0
    idx = 0

    # straight iter doesn't work b/c of changing data
    while not idx >= len(nums):

        # An early out as we change list in place
        if isinstance(nums[idx], str): break

        while nums[idx] == val:
            adjust_slices(idx, nums)
        
        # Only advance when the above condition is False
        idx += 1

    print(nums) # return idx
    print(idx)
    return len([x for x in nums if isinstance(x, int)])


def adjust_slices(idx, nums):
   # repl from 1st dup to end w/last dup to end + x's
   nums[idx:] = nums[idx+1:] + ["x"]


a = [0, 0, 1, 1, 1, 2, 3, 4]
a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

a = [0, 0, 1, 1]
a = [1, 3, 4, 2, 5, 6, 7, 2, 2, 2, 2, 2]
a = [2, 2]
a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
# need to optimize this for ridiculous arrays
# I can optimize by getting a count and then do slicing
print(remove_val_array(a, 100))
