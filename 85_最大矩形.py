from typing import List

from collections import deque
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m, n = len(matrix), len(matrix[0])
        # 先求取left
        left_dp = [[0]*len(matrix[0]) for _ in matrix]
        for r_idx in range(m):
            for c_idx in range(n):
                if matrix[r_idx][c_idx] == '1':
                    left_dp[r_idx][c_idx] = left_dp[r_idx][c_idx-1] + 1 if c_idx>0 else 1
        ret = 0
        for c_idx in range(n):
            upper_bound = [-1 for _ in range(m)]
            lower_bound = [m for _ in range(m)]
            stack = deque()
            for r_idx in range(m):
                while(len(stack) and left_dp[stack[-1]][c_idx] >= left_dp[r_idx][c_idx]):
                    stack.pop()
                upper_bound[r_idx] = stack[-1] if len(stack) > 0 else  upper_bound[r_idx]
                stack.append(r_idx)
            stack.clear()
            for r_idx in range(m-1, -1, -1):
                while(len(stack) and left_dp[stack[-1]][c_idx] >= left_dp[r_idx][c_idx]):
                    stack.pop()
                lower_bound[r_idx] = stack[-1] if len(stack) > 0 else  lower_bound[r_idx]
                stack.append(r_idx)
            ret = max(
                    max(
                        [(lower_bound[r_idx]-upper_bound[r_idx]-1) * left_dp[r_idx][c_idx] 
                        for r_idx in range(m)]),
                ret)
        return ret

sol = Solution()
matrix = [["1","1"]]
ans = sol.maximalRectangle(matrix)
print(ans)