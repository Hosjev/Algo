class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_helper(subarray, placeholder, perms):
            if not subarray and placeholder:
                perms.append(list(placeholder))
                return

            for idx in range(len(subarray)):
                local_subarray = subarray[:idx] + subarray[idx+1:]
                local_placeholder = placeholder + [subarray[idx]]
                permute_helper(local_subarray, local_placeholder, perms)

            return perms

        return permute_helper(nums, [], [])


n = [1, 2, 3, 4]
s = Solution()
ans = s.permute(n)
print(ans)
