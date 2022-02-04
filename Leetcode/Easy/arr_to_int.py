""" Add one to array as whole number """
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not bool(digits): return
        whole_num = int("".join([str(i) for i in digits])) + 1
        return [i for i in str(whole_num)]



if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))
