from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
          return False
        row_idx = bisect.bisect_left([row[0] for row in matrix],target)
        if row_idx!=len(matrix) and matrix[row_idx][0] == target:
            return True
        elif row_idx==0:
            return  False
        else:
            row_idx=row_idx-1
        col_idx = bisect.bisect_left(matrix[row_idx], target)
        if col_idx>=len((matrix[row_idx])) or matrix[row_idx][col_idx]!=target:
            return False
        else:
            return True

sol=Solution()
matrix = [[1]]
ans = sol.searchMatrix(matrix,1)
print(ans)