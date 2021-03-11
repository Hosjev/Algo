"""
Given 2 inputs:
1st == array of "teams (array)"
2nd == array of corresponding winners for that round (indices)
For the second arg, results are as such:
[homeTeam, awayTeam]
[1==home, 0==away]
**each win worth 3
Return winner

Input:
    teams = [
            1     0
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
        ]
    results = [0, 0, 1]
Output:
    "Python"

**one team WILL win
**always at least 2 teams
**got it to O(N)
"""
import time


def _swap(idx):
    return 1 if idx == 0 else 0


def tournamentWinner(competitions, results):
    # Write your code here.
    """
    -unique team
    -specify index
    -tally total for each unique team
    DP with high score? to keep O(n)
    """
    teams = {}

    for idx in range(len(competitions)):
        winner = competitions[idx][_swap(results[idx])]
        try:
            teams[winner] += 1
            # could keep running high scorer to avoid max
        except KeyError:
            teams[winner] = 1

    return max(teams.items(), key=lambda x: x[1])[0]


comps = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
res = [0, 0, 1]

comps = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]
res = [0, 1, 1]

print(tournamentWinner(comps, res))
