class Solution:
    def __init__(self, msg):
        self.msg = msg


    def perform_mod(self, num):
        max_prime_num = (pow(10, 9) + 7)
        return (num % max_prime_num + max_prime_num) % max_prime_num

    
    def decode(self):
        # TODO: store 10^9+7; store table vals in vars
        # Edge Case(s)
        if self.msg[0] == "0": return 0
        # Prime my answer table
        A = [0] * (len(self.msg) + 1)
        A[0], A[1] = 1, 1

        for i in range(2, len(self.msg) + 1):
            ind = int(self.msg[i - 1])
            pair_start = int(self.msg[i - 2])
            if ind > 0:
                A[i] = self.perform_mod(A[i - 1])
            if (pair_start == 1) or (pair_start == 2 and ind < 7):
                A[i] += self.perform_mod(A[i - 2])

        return A[-1]



m = "2059134175"
m = "20591212121212121212121212121212111111111111111112222222222222222222222111111111111111111222222222134175"
m = "081212212"
a = Solution(m)
print(a.decode())
