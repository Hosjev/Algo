class Solution:
    """
    Input: array of prices
    Output: int (profit)
    """
    def maxProfit(self, prices):
        profit = 0
        best_price = prices[0]

        # Move forward and look back
        for idx in range(1, len(prices)):
            # As long as we eval the min first
            best_price = min(best_price, prices[idx])
            profit = max(profit, prices[idx] - best_price) 

        return profit


p = [7, 1, 5, 3, 6, 4]
p = [7, 6, 5, 4, 1]
a = Solution()
print(a.maxProfit(p))
