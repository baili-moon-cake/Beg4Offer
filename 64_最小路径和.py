from itertools import accumulate
from operator import add
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf'),] + list(accumulate(grid[0], add))
        for row in range(1, m):
            for col in range(n):
                dp[col+1] = min(dp[col+1], dp[col]) + grid[row][col]
        return dp[-1]

sol = Solution()
ans = sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(ans)