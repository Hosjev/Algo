from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # EC
        if not bool(nums2): return nums1
        pointer1, pointer2 = m - 1, n - 1
        for placement in range(len(nums1) - 1, -1, -1):
            if pointer2 < 0: break
            if nums1[pointer1] > nums2[pointer2]:
                nums1[placement] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[placement] = nums2[pointer2]
                pointer2 -= 1
        


if __name__ == "__main__":
    n1 = [1, 2, 3, 0, 0, 0]
    n2 = [2, 5, 6]
    obj = Solution()
    obj.merge(n1, 3, n2, 3)
    print(n1)
    n1 = [0, 0]
    n2 = [1]
    obj = Solution()
    obj.merge(n1, 2, n2, 1)
    print(n1)

