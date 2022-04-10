class Solution:
    def plusOne(self, digits) -> list:
        # EC
        # Logic - 1. get pure str, 2. 
        num_str = "".join([str(i) for i in digits])
        num_str = str(int(num_str) + 1)
        return [int(i) for i in num_str]
