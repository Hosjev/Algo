from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # EC
        if not bool(nums2): return nums1
        
        # Prime
        flex = len(nums1) - 1
        P2 = len(nums2) - 1
        try:
            P1 = max([i for i,e in enumerate(nums1) if e])
        except ValueError:
            return nums2

        while not P1 < 0 and not P2 < 0:
            if nums2[P2] > nums1[P1]:
                nums1[flex] = nums2[P2]
                P2 -= 1
            else:
                nums1[flex] = nums1[P1]
                P1 -= 1
                while not nums1[P1]:
                    P1 -= 1
            flex -= 1

        if P1 < 0:
            nums1[0] = nums2[0]
        return nums1


if __name__ == "__main__":
    n1 = [1, 2, 3, 0, 0, 0]
    n2 = [2, 5, 6]
    n1 = [0]
    n2 = [1]
    print(Solution().merge(n1, 6, n2, 3))
