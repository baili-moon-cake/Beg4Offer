from typing import List
class Solution:
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        used = [[False]*n for _ in range(m)]
        cnts = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and used[r][c] is False:
                    self.corefunc(grid, r, c, used)
                    cnts += 1
        return cnts
    def corefunc(self, grid, x, y, used):
        used[x][y] = True
        for offset_x, offset_y in self.direction:
            new_x, new_y = x+offset_x, y+offset_y
            if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and \
                grid[new_x][new_y] == "1" and used[new_x][new_y] is False:
                self.corefunc(grid, new_x, new_y, used)
            
