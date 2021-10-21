class Solution:
    def __init__(self):
        self.roman_hash = {
            "M": 1000, # M
            "CM": 900, # M
            "D": 500,  # D
            "CD": 400,  # D
            "C": 100,  # C
            "XC": 90,  # C
            "L": 50,   # L
            "XL": 40,   # L
            "X": 10,   # X
            "IX": 9,   # X
            "V": 5,    # V
            "IV": 4,    # V
            "I": 1     # I
        }

    def int_roman(self, num):
        # Prime
        r = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        answer = ""

        for k,v in zip(r, i):
          answer += (num // v) * k
          num = num % v
        return answer


# 1915 MCMXV
print(Solution().int_roman(1915))
print(Solution().int_roman(4))
print(Solution().int_roman(5))
