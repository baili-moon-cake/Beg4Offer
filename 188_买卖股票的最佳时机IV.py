class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n<=0:
            return 0
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:  # 初始化i=0的情况
                    dp[0][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]