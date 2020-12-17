from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0]: 第i天为止,不持有股票的最大profit;
        # dp[i][1]: 第i天为止,持有股票的最大profit;
        # 状态转移矩阵:
        # dp[i+1][0] = max(dp[i][1]+p[i+1]-fee, dp[i][0])
        # dp[i+1][1] = max(dp[i][0]-p[i+1], dp[i][1])
        # 最终返回:
        # dp[-1][0]
        # 初始化:
        # dp[0][0], dp[0][1] = 0, -p[0]
        dp = [[0,]*2 for _ in prices]
        dp[0][1] = -prices[0]
        for idx in range(1, len(prices)):
            dp[idx][0] = max(dp[idx-1][1]+prices[idx]-fee, dp[idx-1][0])
            dp[idx][1] = max(dp[idx-1][0]-prices[idx], dp[idx-1][1])
        return dp[-1][0]
 
 
sol = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2000
ans = sol.maxProfit(prices, fee)
print(ans)