from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       # 1. choose larger array to setify, smaller to iterate
       #    a. if == size, def to nums1 larger, num2 smaller
       # 2. iter through answer, if int NOT in nums1, rem
       larger_set = set(nums2) if len(nums2) > len(nums1) else set(nums1)
       smaller = nums1 if len(nums1) < len(nums2) else nums2
       answer = list()
       for i in smaller:
           if i in larger_set:
               answer.append(i)
               larger_set.remove(i)
       return answer


# Version II, return all matches
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       # 1. assume one is too large to fit memory
       # 2. turn arrays into collections
       # 3. same idea as above, iter through smaller list
       from collections import Counter
       hash_of_1, hash_of_2 = Counter(nums1), Counter(nums2)
       large = hash_of_2 if len(hash_of_2) > len(hash_of_1) else hash_of_1
       small = hash_of_1 if len(hash_of_1) < len(hash_of_2) else hash_of_2
       answer = list()
       for i in small:
           if i in large:
               answer += [i] * min(large[i], small[i])
       return answer



if __name__ == "__main__":
    n1 = [4, 4, 9, 5]
    n2 = [9, 4, 9, 8, 4]
    n1 = [1, 2, 2, 1]
    n2 = [2, 2]
    #print(Solution().intersection(n1, n2))
    print(Solution().intersect(n1, n2))
