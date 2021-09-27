class Solution:
    def combinationSum(self, candidates, target):
        """ Summing distinct integers to target using backtracking"""

        def combo_helper(placeholder, rem_sum, current, answer):
            if rem_sum == 0:
                answer.append(list(placeholder))
                return

            for x in range(1):
                ME = candidates[current]
                if rem_sum - ME < 0:
                    break
                placeholder.append(ME)
                combo_helper(placeholder, rem_sum - ME, current, answer)
                placeholder.pop()

                for pointer in range(current + 1, len(candidates)):
                    next_current = candidates[pointer]
                    if rem_sum - next_current < 0:
                        break
                    placeholder.append(next_current)
                    combo_helper(placeholder, rem_sum - next_current, pointer, answer)
                    placeholder.pop()
    

        # Priming
        candidates.sort()
        placeholder, answer = [], []
        combo_helper(placeholder, target, 0, answer)

        return answer


c = [1, 2, 5]
t = 5
s = Solution()
print(s.combinationSum(c, t))
c = [2, 3, 5]
t = 8
s = Solution()
print(s.combinationSum(c, t))
