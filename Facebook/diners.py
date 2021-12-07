from typing import List
# Write any import statements here

class SocialDistance:

    def slow(self):
        for potential in range(1, N + 1):
            occupied = potential in S
            if not occupied and space == K:
                space = 0
                new_diners += 1
            else:
                if not occupied and space < K:
                    space += 1
                elif occupied and space != K:
                    space = 0
                    new_diners -= 1
                else: # occupied and space = K
                    space = 0

    def getMaxAdditionalDinersCount(self, N: int, K: int, M: int, S: List[int]) -> int:
        # INPUT:
        #     N = # seats at table
        #     K = # empty seat(s) for SD
        #     M = # of already seated
        #     S = [] is index of M
        # Inflate S with extra as we move thru occupied and look back
        # OUTPUT: available seats given contraints
        import math
  
        new_diners, start = int(), 1
        space = K
        S.append(N+space+1)
        S.sort()
        for seat in S:
            available = seat - start - space
            if available > 0:
                new_diners += math.ceil(available / (space + 1))
            start = seat + space + 1

        return new_diners


if __name__ == "__main__":
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]

    N = 10
    K = 1
    M = 2
    S = [2, 6]

    print(SocialDistance().getMaxAdditionalDinersCount(N, K, M, S))
