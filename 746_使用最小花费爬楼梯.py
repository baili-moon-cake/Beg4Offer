from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in cost]
        dp[0], dp[1] = cost[0], cost[1]
        for idx, c in enumerate(cost[2:], start=2):
            dp[idx] = c + min(dp[idx-2], dp[idx-1])
        return min(dp[-1], dp[-2])
sol = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
ans = sol.minCostClimbingStairs(cost)
print(ans)
