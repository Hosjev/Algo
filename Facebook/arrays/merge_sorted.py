from typing import List



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        P1, P2 = m - 1, n - 1

        # Logic (iterate in O(N) across nums1)
        for place in range(n + m - 1, -1, -1):
            # we keep track of 2nd list scope here
            if P2 < 0:
                break
            # we keep track of 1st list scope here
            if P1 >= 0 and nums1[P1] > nums2[P2]:
                nums1[place] = nums1[P1]
                P1 -= 1
            else:
                nums1[place] = nums2[P2]
                P2 -= 1


if __name__ == "__main__":
    obj = Solution()
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    print(obj.merge(n1,3,n2,3))
    n1 = [4,5,6,0,0,0]
    n2 = [1,2,3]
    print(obj.merge(n1,3,n2,3))
