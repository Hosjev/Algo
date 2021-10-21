class Solution:
    """
    Input: prices array
    Output: profit int
    """
    def maxProfit(self, prices):
        today = 0
        tomorrow = 0
        profit = 0

        while not today == len(prices) - 1:
            tomorrow = today + 1
            if prices[tomorrow] > prices[today]:
                # Execute buy/sell now
                profit += prices[tomorrow] - prices[today]
            # Move on regardless
            today += 1

        return profit

p = [7, 1, 5, 3, 6, 4]
p = [1, 2, 3, 4, 5]
p = [5, 4, 3, 2, 1]
print(Solution().maxProfit(p))
