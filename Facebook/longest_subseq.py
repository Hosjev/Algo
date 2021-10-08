class Solution:
    def __init__(self, nums):
        self.nums = nums


    def longest_subseq(self):
        # Priming
        # Each number, regardless of value, is ONE advance
        advances = [1] * len(self.nums)

        # Now we count the number of absolute advances
        # looking backward from each index
        for idx in range(1, len(self.nums)):
            for pointer in range(0, idx):
                if self.nums[idx] > self.nums[pointer]:
                    # Add the bounce and myself then compare
                    advances[idx] = max(advances[idx], advances[pointer] + 1)

         # O(N^2)
        return max(advances)


n = [0, 8, 4, 2, 3, 4]
n = [15, 8, 4, 2, 3, 4]
n = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
n = [ 84, 80, 27 ]

a = Solution(n)
print(a.longest_subseq())
