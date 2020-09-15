class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        return self.corefunc(matrix, target, 0, len(matrix[0]))
    def corefunc(self, matrix, target, row, col):
        new_col, new_row = -1, -1
        for c in range(col)[::-1]:
            if matrix[row][c] == target:
                return True
            if matrix[row][c] <target:
                new_col = c
                break
        if new_col == -1:return False
        for r in range(row, len(matrix)):
            if matrix[r][new_col] == target:
                return True
            if matrix[r][new_col] >target:
                new_row = r
                break
        if new_row == -1:return False
        return self.corefunc(matrix, target, new_row, new_col)

sol=Solution()
matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=5
sol.searchMatrix(matrix,5)