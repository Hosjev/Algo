"""
Given an array of positive ints, representing the values of coins in ur pocket, return the minumum amount of change that you CANNOT create. For ex: [1, 2, 5] == 4 and no change == 1.

Input:
    [1, 2, 5]
Output:
    4

"""
import time


def nonConstructibleChange(coins):
    # Write your code here.
    # if we have empty pockets, return 1
    if not coins:
		return 1
    # if we have one coin and > 1,
    # return smallest amount we CANT make 1
    # else it IS 1, return 2
	if len(coins) == 1:
		if coins[0] == 1:
			return 2
        return 1

    def _recur_through_coins(idx, change):
        if ((idx) == len(coins)):
            return (change + 1)

        new_change = change + 1
        if (new_change < coins[idx]):
            return new_change
        else:
            return _recur_through_coins(idx + 1, change + coins[idx])

    coins.sort()
    return _recur_through_coins(0, 0)


c = [1, 1, 4]
c = [1, 1, 3]
c = []
c = [4]
c = [1, 1, 2, 3, 5, 7, 22]
print(nonConstructibleChange(c))
