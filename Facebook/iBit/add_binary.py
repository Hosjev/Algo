class Solution:
    def addBinary(self, a, b):
        def binary_to_decimal(binary):
            decimal, i = 0, 0
            while binary != 0:
                print(binary)
                rem = binary % 10
                decimal = decimal + (rem * pow(2, i))
                binary = binary//10
                i += 1
            return decimal


        def decimal_to_binary(num):
            return bin(num).lstrip("0b").zfill(8)

        # Main
        if len(a) == 0: return b
        if len(b) == 0: return a
        a_dec = binary_to_decimal(int(a))
        b_dec = binary_to_decimal(int(b))
        return decimal_to_binary(a_dec + b_dec)


a = "1010"
b = "1011"
#b = ""
print(Solution().addBinary(a, b))
