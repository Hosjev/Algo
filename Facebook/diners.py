from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # A cafe table consists of row N seats, 1 -> N from L to R.
  # Social distancing guidelines require every person be seated
  #   such that K seats to L and R be empty. Or all if fewer than K.
  # There are M diners seated at table, the iTH is in seat S. No 2
  #   diners are sitting in same seat, and SD is satisfied.
  # Determine the max num of additional diners who can sit at table
  #   w/o SD being violated for any or existing diners, assuming the
  #   existing diners can't move and the addt'l diners will cooperate to
  #   max the amt per-table.
  # INPUT:
  #     N = # seats at table
  #     K = # empty seat(s) for SD
  #     M = # of already seated
  #     S = [] is index of M
  # OUTPUT: available seats given contraints
  
    new_diners = int()
    space = K

    # 1-15 (inclusive)
    # As we look right, we start w/the assumption
    #   that left is not occupied.
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

    return new_diners


if __name__ == "__main__":
    N = 15
    K = 1
    M = 3
    S = [11, 6, 14]

    #N = 10
    #K = 1
    #M = 2
    #S = [2, 6]

    print(getMaxAdditionalDinersCount(N, K, M, S))
