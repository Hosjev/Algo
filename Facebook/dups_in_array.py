class DupsArray:
    """ O(1) """ 
    def check(self, nums):
        # Several solutions
        # return sorted(nums) == sorted(set(nums))
        # make memo table and track count by value/int by key
        # iter straight thru after sort 1->end
        # use math given constraints => in array 1 to N(len)
        # [1,2,3,4,5] == sum(15) == (len(nums)+1)) * (len(nums)/2)
        #                NOT above to produce False
        return self.use_math(nums)

    def use_math(self, nums):
        return not sum(nums) == (len(nums)+1) * (len(nums)/2)


if __name__ == "__main__":
    print(DupsArray().check([1,2,3,4,5]))
