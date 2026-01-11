class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = [(sr,sc)]
        n, m = len(image), len(image[0])
        start_color = image[sr][sc]
        
        def validNeigh(y:int, x:int) -> (int,int):
            for dy,dx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                if 0 <= dx < m and 0 <= dy < n and image[dy][dx] != color and image[dy][dx] == start_color:
                    yield (dy, dx)
            return (-1,-1)
            
        while q:
            y,x = q.pop(0)
            image[y][x] = color
            for dy,dx in validNeigh(y,x):
                q.append((dy,dx))
        return image
