from typing import List
class Solution:
    directions = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land and len(land[0]) == 0:
            return []
        used = [[False for col in row] for row in land]
        ret = []
        self.h, self.w = len(land), len(land[0])
        for row_idx in range(self.h):
            for c_idx in range(self.w):
                if land[row_idx][c_idx] == 0 and  used[row_idx][c_idx] is False:
                    ret.append(self.dfs(land,used,row_idx,c_idx))
                else:
                    used[row_idx][c_idx] = True
        return sorted(ret)

    def dfs(self, land_matrix, used_matrix, row_idx, col_idx):
        if used_matrix[row_idx][col_idx] or land_matrix[row_idx][col_idx]!=0:
            return 0
        used_matrix[row_idx][col_idx] = True
        area = 1
        for row_offset, col_offset in  self.directions:
            new_row_idx, new_col_idx = row_idx+row_offset, col_idx+col_offset
            if new_row_idx >= self.h or new_row_idx <0 or new_col_idx >= self.w or new_col_idx < 0:
                continue
            area+=self.dfs(land_matrix, used_matrix, new_row_idx, new_col_idx)
        return area

sol = Solution()
land = [[0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]]
ans=sol.pondSizes(land)
print(ans)