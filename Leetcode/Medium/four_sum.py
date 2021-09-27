def fours(nums, target):
    """
    Return all target sums from nums in 4s
    """

    if len(nums) < 4: return []

    quadruplets = set()
    diff_hash = {}

    # Priming
    left = 1
    pointer = left + 1
    nums.sort()

    # Outer while
    while left != len(nums) - 1:
        # Inner while forward
        while pointer != len(nums):
            f_sum = nums[left] + nums[pointer]
            try:
                diff_sum = (target) - (f_sum)
                for pair in diff_hash[diff_sum]:
                    quadruplets.add((pair[0], pair[1], nums[left], nums[pointer]))
            except KeyError:
                pass
            pointer += 1

        # Inner while backward
        pointer = 0
        while pointer != left:
            b_sum = nums[pointer] + nums[left]
            try:
                # Optimizing dups
                if not [nums[pointer], nums[left]] in diff_hash[b_sum]:
                    diff_hash[b_sum].append([nums[pointer], nums[left]])
            except KeyError:
                diff_hash[b_sum] = [[nums[pointer], nums[left]]]
            pointer += 1

    
        # Advance outer loop
        left += 1
        pointer = left + 1

    print(diff_hash)
    return [list(x) for x in quadruplets]


n = [-2, -1, 0, 0, 1, 2] # 6
n = [2, 2, 2, 2, 2]
print(fours(n, 8))
t = 0
n = [-5,5,4,-3,0,0,4,-2]
t = 4
print(fours(n, t))
