def remove_dups_array(nums):
    """
    1. set 2 pointers
       a. 1st is set from linear loop
       b. 2nd is set from 1st plus 1
    2. while loop serves to ensure 1st != 2nd
       a. moves on ONLY when any dups of 1st are exhausted
    3. helper function replaces list slices, one at a time
       a. helper also fills out end one at a time w/"x"?
       b. changed to adjust slices only when adjacent dups counted
    """
    if not nums: return 0

    idx1 = 0
    idx2 = idx1 + 1

    while not idx2 == len(nums): # outer while

        print(nums)
        pointer1 = nums[idx1]
        pointer2 = nums[idx2]
        if isinstance(pointer1, str): break

        # Move pointer2
        counter = 0
        while pointer1 == pointer2: # inner while
            counter += 1
            try:
                pointer2 = nums[idx2+counter]
            except IndexError:
                break
        if counter: adjust_slices(idx2, counter, nums)

        # We reset these 2 pointers to left adjacent
        idx1 += 1
        idx2 = idx1 + 1

    print(nums) # you Could return idx1
    print(idx1) # return 1 if idx1 == 0 else idx1
    return len([x for x in nums if isinstance(x, int)])


def adjust_slices(idx2, counter, nums):
   # Slow
   # nums[idx2:] = nums[idx2+1:] + ["x"]
   # repl from 1st dup to end w/last dup to end + x's
   nums[idx2:] = nums[idx2+counter:] + ["x"] * counter


a = [0, 0, 1, 1, 1, 2, 3, 4]
a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

a = [0, 0, 1, 1]
a = [1, 2, 2]
a = [1, 1]
a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
a = [1, 2, 2]
a = [1, 1]
a = [0]
# need to optimize this for ridiculous arrays
# I can optimize by getting a count and then do slicing
print(remove_dups_array(a))
