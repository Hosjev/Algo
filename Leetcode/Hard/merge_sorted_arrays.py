class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        from math import floor

        nums1 += nums2
        nums1.sort()

        # Even
        if len(nums1) % 2 == 0:
            middle = int(len(nums1) / 2)
            median = (nums1[middle - 1] + nums1[middle]) / 2
        # Odd
        else:
            middle = int(floor(len(nums1) / 2))
            median = nums1[middle]

        return float(median)


n1 = [1,3]
n2 = [2]
n1 = [1, 2]
n2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(n1, n2))
