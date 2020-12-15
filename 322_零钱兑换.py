from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount in coins:
            return 1
        if len(coins) == 0:
            return -1 
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for idx in range(1, amount+1):
            min_list = [
                dp[idx-coin] for coin in coins 
                if idx-coin>=0 and dp[idx-coin]!=-1
            ]
            dp[idx] = min(min_list) + 1 if min_list else -1
        return dp[amount]

sol = Solution()
coins = [2,]
amount = 3
ans = sol.coinChange(coins, amount)
print(ans)