class ChangeMaker:

    def ways_of(self, coins, money):
        if not coins: return 0
        units = [0] * (money + 1)
        units[0] = 1 # Prime for OF money
        for denomination in coins:
            for unit in range(len(units)):
                if denomination <= unit:
                    # Forward tally
                    units[unit] += units[unit - denomination]

        return units[-1]


def main():
    c = [1, 5, 25, 50]
    m = 10
    print(ChangeMaker().ways_of(c, m))


main()
