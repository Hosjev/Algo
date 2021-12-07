from typing import List


class Solution:
    def _recurse(self, idx, placeholder, array, combos):
        if len(placeholder) == len(array):
            combos.append(placeholder)
            return combos

        for i in array[idx]:
            local = placeholder + i
            self._recurse(idx + 1, local, array, combos)
        return combos

    def letterCombinations(self, digits: str) -> List[str]:
        # Edge Case(s)
        if not bool(digits): return []
        translate = {
                "0": "0",
                "1": "1",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
              }
        alpha = [translate[i] for i in digits]
        return self._recurse(0, "", alpha, []) 


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
