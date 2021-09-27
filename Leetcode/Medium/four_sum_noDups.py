class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        This algorithm works for non-distinct ints.
        For distinct nums, use lists instead of sets
        """
        def eval_difference(t, one, two):
            return t - ((one) + (two))


        def add_to_quads(sets, pair, quadruplets):
            for item in sets:
                quadruplets.add(tuple(sorted([item[0], item[1], pair[0], pair[1]])))


        # Edge case
        if len(nums) < 4: return []

        # Priming
        quadruplets = set()
        two_sum_hash = dict()

        # Outer Loop
        static = 1
        while not static == len(nums):

            # Inner Loop forward
            moving = static + 1
            while not moving == len(nums):
                diff = eval_difference(target, nums[static], nums[moving])
                try:
                    add_to_quads(two_sum_hash[diff], [nums[static], nums[moving]], quadruplets)
                except KeyError:
                    pass
                moving += 1

            # Inner Loop backward
            moving = 0
            while not moving == static:
                pair_sum = (nums[static]) + (nums[moving])
                try:
                    two_sum_hash[pair_sum].add(tuple(sorted([nums[moving], nums[static]])))
                except KeyError:
                    two_sum_hash[pair_sum] = set()
                    two_sum_hash[pair_sum].add(tuple(sorted([nums[moving], nums[static]])))
                moving += 1

            static += 1

        return [list(x) for x in quadruplets]



n = [1, 0 ,-1, 0, -2, 2, -1]
a = Solution()
print(a.fourSum(n, 0))
n = [2, 2, 2, 2, 2, 2]
a = Solution()
print(a.fourSum(n, 8))
