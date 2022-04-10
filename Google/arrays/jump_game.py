from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # EC
        if not bool(nums): return False
        if len(nums) == 1:
            return True

        # Prime
        can_go_to_index, steps_avail = nums[0], nums[0]
        jump = int()
        idx = 1

        # Logic
        while idx < len(nums):
            can_go_to_index = max(can_go_to_index, nums[idx] + idx)
            steps_avail -= 1
            # Last index condition
            if idx == len(nums)-1:
                if steps_avail < 0: jump = 0
                else: jump += 1
            else:
                if steps_avail == 0:
                    jump += 1
                    steps_avail = can_go_to_index - idx
            idx += 1

        return True if jump else False


if __name__ == "__main__":
    n = [3,2,1,0,4]
    obj = Solution()
    print(obj.canJump(n))
    n = [3,2,1,1,4]
    obj = Solution()
    print(obj.canJump(n))
    n = [2,3,1,1,4]
    obj = Solution()
    print(obj.canJump(n))
    n = [4,0,0,0,4]
    obj = Solution()
    print(obj.canJump(n))
    n = [1,1,0,1]
    obj = Solution()
    print(obj.canJump(n))
