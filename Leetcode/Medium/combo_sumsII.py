class Solution:
    def combinationSum2(self, candidates, target):
        """ Summing non-distinct integers to target using backtracking """
        def combo_helper(placeholder, rem_sum, current, answer):
            if rem_sum == 0:
                answer.append(list(placeholder))
                return

            for pointer in range(current, len(candidates)):
                if (pointer > current) and \
                    (candidates[pointer] == candidates[pointer-1]):
                    continue
                next_int = candidates[pointer]
                if rem_sum - next_int < 0:
                    break
                placeholder.append(next_int)
                combo_helper(placeholder, rem_sum - next_int, pointer + 1, answer)
                placeholder.pop()


        # Priming
        candidates.sort()
        placeholder, answer = [], []
        combo_helper(placeholder, target, 0, answer)

        return answer

c = [1, 2, 2, 2, 5]
t = 5
s = Solution()
print(s.combinationSum2(c, t))
c = [10,1,2,7,6,1,5]
#c = [1, 1, 2, 5, 6, 7, 10]
t = 8
s = Solution()
print(s.combinationSum2(c, t))
