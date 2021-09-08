from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    """
    In the first case, it's possible that there are as few as 4 problems in the contest.
    For example with point values [1, 1, 2, 2].
    The 6 competitors could have solved the following subsets of problems:
    Problem 1 (1 point)
    Problem 3 (2 points)
    Problems 2 and 3 (1 + 2 =3 points)
    Problems 1, 2, and 4 (1 + 1 + 2 = 4 points)
    Problems 2, 3, and 4 (1 + 2 + 2 = 5 points)
    All 4 problems (1 + 1 + 2 + 2 = 6 points)
    It is impossible for all 6 competitors to have achieved their scores if there are fewer than 4 problems.
    """
    # Write your code here
    # N = number of competitors
    # S = their scores
    # each problem solved earns 1 or 2 points
    # OUTPUT: minimum number of problems based on scores/players
    # N = 6
    # S = [1, 2, 3, 4, 5, 6]
    # Ans = 4
    # N = 4
    # S = [4, 3, 3, 4]
    # 3
    # N = 4
    # S = [2, 4, 6, 8]
    # 4
    # This feels like a non-DP answer but ...
    min_rounds = int(max(S) / 2)
    odds = False
    for i in S:
        if (i % 2 != 0):
            odds = True

    return min_rounds if not odds else min_rounds + 1

print(getMinProblemCount(4, [2, 4, 6, 8]))
