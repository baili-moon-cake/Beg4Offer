from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[],]
        elif numRows == 1:
            return [[1,]]
        elif numRows == 2:
            return [[1,],[1,1]]
        ret = [[1,],[1,1]]
        for row_idx in range(2, numRows):
            tmp_row = [1,]
            for col_idx in range(len(ret[row_idx-1])-1):
                tmp_row.append(
                    ret[row_idx-1][col_idx] + \
                    ret[row_idx-1][col_idx+1])
            tmp_row.append(1)
            ret.append(tmp_row)
        return ret
