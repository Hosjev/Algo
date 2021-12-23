from typing import List



class Solution:
    """ Eval all possible perms of operator combos """
    def _recurse(self, pointer, num, target, ph, results):
        if pointer == len(num):
            ph.pop(0)
            string = "".join(ph)
            t_sum = eval(string[0:3])
            for i in range(3, len(string), 2): # step by 2
                t_sum = eval(f'{t_sum} {string[i]} {string[i+1]}')
            if t_sum == target: results.append(string)
            return results
        # Loop
        for operator in ["*", "+", "-"]:
            local_ph = ph + [operator] + [num[pointer]]
            self._recurse(pointer + 1, num, target, local_ph, results)
            local_ph.pop()
            local_ph.pop()
            # Our placeholder eventually empties, let's exit
            if not bool(local_ph): return results

    def addOperators(self, num: str, target: int) -> List[str]:
        # Fairly gross TC of O(n^3 + ^len of str) operators
        # Edge Case(s)
        if not bool(num): return []

        # Logic
        return self._recurse(0, num, target, [], [])



if __name__ == "__main__":
    n = "123"
    t = 6
    print(Solution().addOperators(n, t))
