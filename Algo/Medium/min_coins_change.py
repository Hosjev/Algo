"""
Given an array of distinct positive ints representing coin denominations and a single
non-negative int representing a target amount of money, write a function that returns
the number of ways to make change for (to sum up to) that target amount using the given coinage.

Input:
    n = 7
    denoms = [1, 5, 10]
Output:
    3 # 2x1 + 1x5

* return -1 if you can't make change with the coinage
* Dynamic Programming
answer - O(N)T O(d)S --N=nodes, d=depth
"""


def minNumberOfCoinsForChange(money, change):
    # Make new array for reaching every stage of the final sum
    #     zero to inclusive of final number
    # Make sure it's hard to reach a minimum
    infinity = float("inf")
    individual_sums = [infinity for x in range(money+1)]
    individual_sums[0] = 0
    for denom in sorted(change):
        # iterate through each sum
        # and if my denomination is within my sum, act
        # HERE, idx IS our sum
        # What we store here is our # of coins/dollars/whatever units
        print(f"Processing denom: {denom}")
        for unit in range(len(individual_sums)):
            if denom <= unit:
                print(f"...denom within sum: {unit}")
                diff = unit - denom
                individual_sums[unit] = min(individual_sums[unit], (1 + individual_sums[diff]))

    return individual_sums[-1] if individual_sums[-1] != infinity else -1


if __name__ == "__main__":

    array = [1, 5]
    money = 6
    array = [2, 3, 7]
    money = 0
    array = [2, 4]
    money = 7


    print(minNumberOfCoinsForChange(money, array))
