#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """Strategy1:BFS
        Runtime: O(nm), 
        Space: O(nm)

        Args:
            image (List[List[int]]): an m by n image grid
            sr (int): starting row
            sc (int): starting col
            newColor (int): color to assign

        Returns:
            List[List[int]]: a new image flled by new color from starting position.
        """

        n, m = len(image), len(image[0])
        queue = [(sr, sc)]
        new_image = [[image[y][x] for x in range(m)] for y in range(n)]
        new_image[sr][sc] = newColor
        initColor = image[sr][sc]

        def validNeighs(y, x):
            for r, c in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                if 0 <= r < n and 0 <= c < m and new_image[r][c] == initColor \
                        and new_image[r][c] != newColor:
                    yield r, c

        while queue:
            y, x = queue.pop()
            for r, c in validNeighs(y, x):
                new_image[r][c] = newColor
                queue.append((r, c))
        return new_image
# @lc code=end
