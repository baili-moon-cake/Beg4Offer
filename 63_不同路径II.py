from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid)==0:
            return 0
        elif len(obstacleGrid)==1:
            return 0 if any(obstacleGrid[0]) else 1
        elif obstacleGrid[0][0] == 1:
            return 0
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)], [0 for _ in range(n+1)]]
        dp[0][0] = 0
        for idx, v in enumerate(obstacleGrid[0]):
            if v:
                break
            else:
                dp[0][idx+1]=1
        for row in range(1,m):
            for col in range(n):
                if obstacleGrid[row][col]:
                    dp[row%2][col+1] = 0
                else:
                    dp[row%2][col+1] = dp[1-row%2][col+1]+dp[row%2][col]
        return dp[(m-1)%2][-1]
sol = Solution()
inp = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
ans = sol.uniquePathsWithObstacles(inp)
print(ans)