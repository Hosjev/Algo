class BitSwap:
    # Code wrong or output wrong
    def pairwise_swap(self, b_num):
        if not b_num:
            raise TypeError("Duuuh. We need num, bruh.")
        if b_num == 0 or b_num == 1:
            return b_num
        odd = (int(b_num) & int('1010101010101010', 2)) >> 1
        even = (int(b_num) & int('0101010101010101', 2)) << 1
        return bin(odd | even).replace('0b', '')


bs = BitSwap().pairwise_swap('0000100111110110')
print(bs)
