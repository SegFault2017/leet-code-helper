#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List


class Solution:
    def BFS(self, grid: List[List[int]]) -> int:
        """Strategy 2: BFS
        Runtime: O(n*m),where n is the # of rows fo grid, and m is the number
         of columns fo grid
        Space:O(m*n)

        Args:
            grid (List[List[int]]): grid of 0s(WATER) and 1s(LAND)

        Returns:
            int: the largest area of the grid
        """
        n, m = len(grid), len(grid[0])
        WATER, LAND = 0, 1

        def validNeighs(y: int, x: int) -> tuple:
            for r, c in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                if 0 <= r < n and 0 <= c < m and grid[r][c] == LAND:
                    yield r, c

        def BFS(y: int, x: int) -> int:
            queue = [(y, x)]
            area = 0
            grid[y][x] = WATER
            while queue:
                r, c = queue.pop(0)

                area += 1
                for ny, nx in validNeighs(r, c):
                    grid[ny][nx] = WATER
                    queue.append((ny, nx))
            return area

        largest = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == LAND:
                    largest = max(largest, BFS(y, x))
        return largest

    def DFS(self, grid: List[List[int]]) -> int:
        """Strategy 2: DFS
        Runtime: O(n*m),where n is the # of rows fo grid, and m is the number
         of columns fo grid
        Space:O(m*n)

        Args:
            grid (List[List[int]]): grid of 0s(WATER) and 1s(LAND)

        Returns:
            int: the largest area of the grid
        """
        n, m = len(grid), len(grid[0])
        WATER = 0
        LAND = 1

        def vaildNeighs(y: int, x: int) -> tuple:
            for r, c in [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]:
                if 0 <= r < n and 0 <= c < m and grid[r][c] == LAND:
                    yield (r, c)

        def dfs(y: int, x: int) -> int:
            if grid[y][x] == WATER:
                return 0

            area = 1
            grid[y][x] = WATER
            for r, c in vaildNeighs(y, x):
                area += dfs(r, c)
            return area

        largest = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == LAND:
                    area = dfs(y, x)
                    largest = max(largest, area)
        return largest

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.DFS(grid)
        # @lc code=end
