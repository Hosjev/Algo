"""
Given an array of distinct positive ints representing coin denominations and a single
non-negative int representing a target amount of money, write a function that returns
the number of ways to make change for that target amount using the given coinage.

Input:
    n = 6
    denoms = [1, 5]
Output:
    2 # 1x1 + 1x5 and 6x1

* you have an unlimited amount of coins
* Dynamic Programming
answer - O(N)T O(d)S --N=nodes, d=depth
"""


def numberOfWaysToMakeChange(array, money):

    units_in_money = [ 0 for x in range(money+1)]
    # [0, 0, 0, 0...]

    # Initialize zero dollar to one
    units_in_money[0] = 1
    for denomination in array:
        # Is my change within the unit?
        # The INDEX is my amount
        for unit in range(len(units_in_money)):
            if denomination <= unit:
                # If so, add the remaining denomination count to mine to get another change combo
                #units_in_money[unit] = units_in_money[unit] + units_in_money[unit-denomination]
                units_in_money[unit] += units_in_money[unit-denomination]

    return units_in_money[-1]



if __name__ == "__main__":

    array = [1, 5]
    money = 6
    array = [2, 3, 7]
    money = 0


    print(numberOfWaysToMakeChange(array, money))
