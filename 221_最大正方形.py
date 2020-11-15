from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        n_row, n_col = len(matrix), len(matrix[0])
        dp = [[0,]*n_col for _ in range(n_row)]
        max_square_length = 0
        for _idx in range(n_col):
            if matrix[0][_idx] == '1':
                dp[0][_idx] = 1
                max_square_length = 1

        for _idx in range(n_row):
            if matrix[_idx][0] == '1':
                dp[_idx][0] = 1
                max_square_length = 1

        for r in range(1, n_row):
            for c in range(1, n_col):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                    max_square_length = dp[r][c] if dp[r][c] > max_square_length else max_square_length
        return max_square_length**2

sol = Solution()
inp = [
    ["1"]
    ]

ans = sol.maximalSquare(inp)
print(ans)
