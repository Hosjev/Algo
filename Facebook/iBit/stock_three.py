class Solution:
    """
    Input: prices array
    Output: profit int
    """
    def maxProfit(self, prices):
        one_buy = two_buy = float("inf")
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit


p = [3, 3, 5, 0, 0, 3, 1, 4]
#p = [1, 2, 3, 4, 5]
p = [6,1,3,2,4,7] # 7
print(Solution().maxProfit(p))
