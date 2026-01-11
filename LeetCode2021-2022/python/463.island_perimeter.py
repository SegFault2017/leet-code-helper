class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        preimeter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    preimeter +=4
                    if i > 0 and grid[i-1][j] == 1:
                        preimeter -=2
                    if j > 0 and grid[i][j-1]:
                        preimeter -=2
        return preimeter
