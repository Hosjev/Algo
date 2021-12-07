class Solution:

    def convert_decimals(self, num, idx, answer):
        if idx == len(num):
            return answer
        multi = "1" + (idx * "0")
        answer += (num[idx] * int(multi))
        return self.convert_decimals(num, idx + 1, answer)

    def multiply(self, s1, s2):
        # EC
        if s1 == "0" or s2 == "0":
            return str(0)

        # Prime
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

        # 25 [5, 2]
        h1 = [int_hash[x] for x in reversed(s1)]
        h1_int = self.convert_decimals(h1, 0, 0)
        h2 = [int_hash[x] for x in reversed(s2)]
        h2_int = self.convert_decimals(h2, 0, 0)
        print(h1_int, h2_int)
        return str(h1_int * h2_int)


if __name__ == "__main__":
    print(Solution().multiply("25", "5"))
