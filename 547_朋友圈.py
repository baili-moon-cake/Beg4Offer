from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        knowned = [False for _ in range(len(M))]
        cnts = 0
        for row_idx in range(len(M)):
            if not knowned[row_idx]:
                self.dfs(M,knowned,row_idx) 
                cnts += 1
        return cnts

    def dfs(self, M, knowned, row_idx):
        knowned[row_idx] = True
        for col_idx, realation in enumerate(M[row_idx]):
            if realation == 1 and not knowned[col_idx]:
                self.dfs(M, knowned, col_idx)
sol = Solution()
M = [[1,1,0],
 [1,1,1],
 [0,1,1]]
ans = sol.findCircleNum(M)
print(ans)