def threes(nums, target):
    """
    Return CLOSEST three sum to target
    ** O(N^2) -- best TC
    """


    # Edge case
    if len(nums) < 3: return []
    if len(nums) == 3: return sum(nums)

    # Priming
    answer = [float("inf"), float("inf")]
    nums.sort()

    # Outer pointer
    for pointer in range(len(nums) - 2):
        L = pointer + 1
        R = len(nums) - 1
        while L < R:
            n_sum = nums[pointer] + nums[L] + nums[R]
            if n_sum == target: return target
            steps = abs(n_sum - (target))

            if steps < answer[1]:
                answer[0], answer[1] = n_sum, steps

            # Now we do some intelligent-ish moving
            if n_sum < target:
                L += 1
            else:
                R -= 1

    return answer[0]


n = [-4, -1, 1, 2]
t = 1
n = [0, 0, 0]
t = 1
print(threes(n, t))
