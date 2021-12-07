class TwoPair:
    """ O(N + N//2) """
    def matches(self, nums, k):
        # If nums not sorted, SORT
        # Edge Case(s)
        if len(nums) <= 1:
            return -1
        
        # My cache will hold Target-i = difference key = (8-1=7) / val = 1
        cache = dict()
        for i in nums:
            cache[(k - i)] = i
            
        pair_sets = set()
        for i in range(len(nums)//2):
            key = nums[i] # just me
            if (key in cache) and cache[key] != key:
                pair = tuple(sorted([key, cache[key]]))
                pair_sets.add(pair)
        return pair_sets
    
    
obj = TwoPair()
print(obj.matches([1,2,3,4,5,6,7], 8))
