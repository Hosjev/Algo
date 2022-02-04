from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # EC
        # Prime
        left = [0] * len(height)
        right = [0] * len(height)
        total = int()

        # Logic
        for i in range(1, len(height)):
            left[i] = max(height[i-1], left[i-1])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i+1], right[i+1])

        for i in range(len(height)):
            min_wall = min(left[i], right[i])
            if height[i] < min_wall:
                total += min_wall - height[i]

        return total


if __name__ == "__main__":
    h = [0,1,0,2,1,0,1,3,2,1,2,1]
    obj = Solution()
    print(obj.trap(h))
