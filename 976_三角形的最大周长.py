from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for idx in range(len(A)-1, 1, -1):
            if A[idx] < \
                A[idx-1] + A[idx -2]:
                return A[idx] + \
                    A[idx-1] + A[idx -2]
        return 0

sol = Solution()
inp = [2,1,2]
ans = sol.largestPerimeter(inp)
print(ans)
