class Solution:
    
    def _add_recurse(self, nth, c, of_int, result):
        if nth == c:
            return result
        return self._add_recurse(nth, c + 1, of_int, result + of_int)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Prime
        N = len(num1) + len(num2)
        answer = [0] * N
        
        # Reverse num1 and num2
        # 25 becomes 52; 12 becomes 21 = 300
        # So that we add 5 2
        #                2 1
        #    left-most first
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        for place2, digit2 in enumerate(second_number):
            for place1, digit1 in enumerate(first_number):
                num_zeros = place1 + place2
                carry = answer[num_zeros]
                # To truly use non-multiplier, below would be a recursive add
                # multi_res = self._add_recurse(digit1, 0, digit2, 0)
                # and to improve runtime, choose smaller digit as nth min/max
                #multiplication = int(digit1) * int(digit2) + carry
                s = min(int(digit1), int(digit2))
                l = max(int(digit1), int(digit2))
                multiplication = self._add_recurse(s, 0, l, 0) + carry
                answer[num_zeros] = multiplication % 10
                answer[num_zeros + 1] += multiplication // 10
        
        # Pop the excess 0 from the end of answer.
        if answer[-1] == 0:
            answer.pop()
            
        return ''.join(str(digit) for digit in reversed(answer))



if __name__ == "__main__":
    print(Solution().multiply("25", "12"))
