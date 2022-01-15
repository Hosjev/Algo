class Solution:
    def __init__(self):
        self.roman_hash = {
            "M": 1000, # M
            "D": 500,  # D
            "C": 100,  # C
            "L": 50,   # L
            "X": 10,   # X
            "V": 5,    # V
            "I": 1     # I
        }

    def roman(self, string) -> int:
        last_int = self.roman_hash["M"]
        answer_sum = 0

        for roman_numeral in s:
            current_int = self.roman_hash[roman_numeral]
            answer_sum += current_int
            # if current value is greater than last
            if current_int > last_int:
                answer_sum -= (last_int * 2)
            last_int = self.roman_hash[roman_numeral]

        return answer_sum


s = "MCMXV" # 1915
print(Solution().roman(s))
