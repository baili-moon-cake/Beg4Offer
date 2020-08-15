class Solution:
    def maxProfit(self, prices: List[int]):
        if not prices:
            return 0
        dp = [0] * (len(prices))
        buyPrice = prices[0]
        for idx in range(1, len(prices)):
            if buyPrice < prices[idx]:
                dp[idx] = dp[idx-1] + prices[idx]-buyPrice
                buyPrice = prices[idx]
            else:
                buyPrice = prices[idx]
                dp[idx] = dp[idx-1]
        return dp[-1]