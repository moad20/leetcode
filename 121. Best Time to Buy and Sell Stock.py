class Solution(object):
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        buy = prices[0]
        for i in range(1, len(prices)):
            dp[i] = prices[i] - buy
            buy = min(buy, prices[i])
        return max(dp)