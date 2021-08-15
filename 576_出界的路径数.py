## dfs解法
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         self.height = m
#         self.width = n

#         return int(self.dfs(startColumn, startRow, maxMove) % (1e10 + 7))

#     def dfs(self, x, y, moveCnts):
#         if x < 0 or x >= self.width or \
#             y < 0 or y >= self.height:
#             return 1
#         ret = 0
#         if moveCnts == 0:
#             return ret
#         else:
#             ret += self.dfs(x-1, y, moveCnts-1) + \
#                     self.dfs(x+1, y, moveCnts-1) + \
#                     self.dfs(x, y-1, moveCnts-1) + \
#                     self.dfs(x, y+1, moveCnts-1)
#         return ret

# 动态规划解法
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]
        # self.dp = [[[0,]*n,]*m,]*2
        self.dp[0][startRow][startColumn] = 1
        self.ret = 0        
        self.rows, self.cols = m, n
        for i in range(maxMove):
            idx = i % 2
            self.dp[1-idx] = [[0 for _ in range(n)] for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    val = self.dp[idx][r][c]
                    if val != 0:
                        self.dp_func(r, c, idx, val)
        return int(self.ret % (10**9 + 7))

    def dp_func(self, x, y, idx, val):
        if 0<= x - 1 < self.rows:
            self.dp[1-idx][x - 1][y] += val
        else:
            self.ret += val
        if 0<= x + 1 < self.rows:
            self.dp[1-idx][x + 1][y] += val
        else:
            self.ret += val
        if 0<= y - 1 < self.cols:
            self.dp[1-idx][x][y - 1] += val
        else:
            self.ret += val
        if 0<= y + 1 < self.cols:
            self.dp[1-idx][x][y + 1] += val
        else:
            self.ret += val


sol = Solution()
ans = sol.findPaths(8,50,23,5,26)
print(ans)