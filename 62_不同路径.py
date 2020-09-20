# # DFS解法，时间会超时
# class Solution:
#     directions = [(1,0),(0,1)]
#     valid_path = 0
#     def uniquePaths(self, m: int, n: int):
#         self.final = [m-1,n-1]
#         self.dfs(0,0)
#         return self.valid_path
#     def dfs(self, m, n):
#         # if m>self.final[0] or m<0:
#         if [m,n] == self.final:
#             self.valid_path+=1
#             return
#         for next_step in self.directions:
#             new_m,new_n = m+next_step[0],n+next_step[1]
#             if new_m>self.final[0] or new_m<0 or \
#                 new_n>self.final[1] or new_n<0:
#                 continue
#             self.dfs(new_m, new_n)
# 动态规划解法
class Solution:
    def uniquePaths(self, m: int, n: int):
        if m==1 or n==1:
            return 1
        dp = [[1 for _ in range(n+1)],[0 for _ in range(n+1)]]
        dp[0][0] = 0
        for row in range(1,m):
            for col in range(n):
                dp[row%2][col+1] = dp[1-row%2][col+1]+dp[row%2][col]
        return dp[(m-1)%2][-1]

sol=Solution()
ans = sol.uniquePaths(7,3)
print(ans)