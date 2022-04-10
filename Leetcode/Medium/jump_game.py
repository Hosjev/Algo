class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        THIS SHIT IS BROKE
        """
        # Edge case(s)
        if nums[0] == 0 or len(nums) == 1:
            return 0

        # Priming
        can_go = nums[0]
        steps_available = nums[0]
        jumps = int()
        idx = 1

        # Go forward and look back
        while not idx == len(nums):

            can_go = max(can_go, nums[idx] + idx)
            steps_available -= 1
            # We hit last index BUT we have steps to take
            if idx == len(nums) - 1 and steps_available != 0:
                jumps += 1
            if steps_available == 0:
                # Reset our available stretch
                jumps += 1
                steps_available = can_go - idx # Myself

            idx += 1

        return 1 if jumps == 0 else jumps


n = [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 4] # 6
n = [2, 3, 1, 1, 4]
n = [3, 2, 1, 0, 4]
s = Solution()
print(s.jump(n))
