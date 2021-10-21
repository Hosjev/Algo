class Solution:
	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):
            results = []
            phone_hash = {
                0: ["0"],
                1: ["1"],
                2: ["a", "b", "c"],
                3: ["d", "e", "f"],
                4: ["g", "h", "i"],
                5: ["j", "k", "l"],
                6: ["m", "n", "o"],
                7: ["p", "q", "r", "s"],
                8: ["t", "u", "v"],
                9: ["w", "x", "y", "z"]
            }

            def phone_helper(str_obj, idx):
                if len(str_obj) == len(A):
                    results.append(''.join(str_obj))
                    return

                for char in phone_hash[int(A[idx])]:
                    str_obj.append(char)
                    phone_helper(str_obj, idx + 1)
                    str_obj.pop()

                return results

            # Main - O(N=> * each len hashkey)
            # Edge Case(s)
            return phone_helper([], 0)


A = "034"
# adg adh adi aeg aeh aei afg afh afi
print(Solution().letterCombinations(A))
