class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def verify_valid(s, stack):
            for character in s:
                if character == "(":
                    stack.append(character)
                else:
                    # Right Side
                    try:
                        stack.pop()
                    except IndexError:
                        return False
            return True if not stack else False
        

        def permute_helper(subarray, placeholder, perms):
            if not subarray and placeholder:
                perms.append("".join(placeholder))
                return

            for idx in range(len(subarray)):
                local_subarray = subarray[:idx] + subarray[idx+1:]
                local_placeholder = placeholder + [subarray[idx]]
                permute_helper(local_subarray, local_placeholder, perms)

            return perms

        # Main logic
        # Edge case
        if n == 1: return ["()"]

        # Priming --cut down on RT by removing ends
        array = ["("] * (n-1) + [")"] * (n-1)
        uniques = permute_helper(array, [], [])
        print("Built:", len(uniques))

        # Setify the answer then add ends
        uniques = list(set(uniques))
        for i, e in enumerate(uniques):
            uniques[i] = "(" + e + ")"
        print("Setified")

        # Remove invalid parens
        answer = []
        for idx, sets in enumerate(uniques):
            if verify_valid(sets, []):
                answer.append(sets)

        return answer


n = ["()","()", "()"]
n = ["(", "(", ")", ")"]
s = Solution()
print(s.generateParenthesis(6))
