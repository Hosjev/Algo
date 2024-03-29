class Solution:
    """ O(N * N/2) """
    def __init__(self, nums):
        self.nums = nums

    def longest_subseq(self):
        advances = [1] * len(self.nums)

        count = 0
        for idx in range(1, len(self.nums)):
            for pointer in range(0, idx):
                count += 1
                if self.nums[idx] > self.nums[pointer]:
                    advances[idx] = max(advances[idx], advances[pointer] + 1)

        print(count)
        return max(advances)


if __name__ == "__main__":
    n = [0, 8, 4, 2, 3, 4]
    n = [15, 8, 4, 2, 3, 4]
    n = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    print(len(n))
    a = Solution(n)
    print(a.longest_subseq())
