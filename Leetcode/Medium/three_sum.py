def threes(nums):
    """ Add 3 nums in arr to get 0, no dups """
    # Edge Case
    if len(nums) < 3: return []

    # Super important! for this Algo
    nums.sort()
    answer = set()

    for pointer in range(len(nums) - 2):
        L = pointer + 1
        R = len(nums) - 1
        while L < R:
            one, two, three = nums[pointer], nums[L], nums[R]
            t_sum = one + two + three
            if t_sum == 0:
                answer.add((one, two, three))
                L += 1
                R -= 1
            elif  t_sum < 0:
                L += 1
            else:
                R -= 1

    return [list(x) for x in answer]



n = [-1, 0, 1, 2, -1, -4]
#n = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(threes(n))
