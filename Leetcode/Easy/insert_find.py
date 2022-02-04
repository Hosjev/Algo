class Solution:

    def _binary_search(self, L, R, nums, T):
        if L == R:
            if L == len(nums) - 1 and T > nums[L]:
                return L + 1
            else: return L
        M = (L + R) // 2
        if nums[M] == T:
            return M
        elif nums[M] > T:
            return self._binary_search(L, M - 1, nums, T)
        else:
            return self._binary_search(M + 1, R, nums, T)

    def insert_or_find(self, nums, target):
        return self._binary_search(0, len(nums) - 1, nums, target)


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



if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7] # indices
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    a = [1, 2, 3, 5, 6, 7, 9, 10, 11]
    t = 8
    a = [1]
    t = 0
    a = [1, 2, 3]
    t = 0
    a = [1, 3, 5, 8]
    t = 0
    obj = Solution()
    print(obj.insert_or_find(a, t))
    
    # 1st problem -- end of array
    print(insert_or_find([1, 3, 5, 6], 7))
    print(insert_or_find([1, 3, 5, 8], 7))
