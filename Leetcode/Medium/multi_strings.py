class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """


        def convert_decimals(num, idx, answer):
            # Return the places to #s via indices (recursive)
            # TODO: turn int ref below to hash lookup
            if idx == len(num):
                return answer
            multi = "1" + (idx * "0")
            answer += (num[idx] * int(multi))
            return convert_decimals(num, idx + 1, answer)

        # Edge case
        if num1 == "0" or num2 == "0":
            return str(0)


        int_hash = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        h1 = [int_hash[x] for x in reversed(num1)]
        h2 = [int_hash[x] for x in reversed(num2)]
        return str((convert_decimals(h1, 0, 0)) * (convert_decimals(h2, 0, 0)))

n = "234"
n2 = "33"
n = "0"
n2 = "0"
n = "408"
n2 = "5"
s = Solution()
print(s.multiply(n, n2))
