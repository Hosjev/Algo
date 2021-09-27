class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_helper(subarray, placeholder, perms):
            if not subarray and placeholder:
                perms.append(list(placeholder))
                return

            for idx in range(len(subarray)):
                # Skip entire branches if last int matches
                if len(subarray) > 1 and subarray[idx] == subarray[idx-1]:
                    if not idx == 0:
                        continue
                local_subarray = subarray[:idx] + subarray[idx+1:]
                local_placeholder = placeholder + [subarray[idx]]
                permute_helper(local_subarray, local_placeholder, perms)

            return perms

        nums.sort()
        return permute_helper(nums, [], [])


n = [1, 2, 3]
n = [3, 3, 0, 3]
n = [1, 1, 2]
n = [1, 2, 3]
s = Solution()
print(s.permuteUnique(n))
