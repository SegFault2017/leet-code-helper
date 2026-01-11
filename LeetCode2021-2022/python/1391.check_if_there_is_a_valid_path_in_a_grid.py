class Solution:
    from collections import deque
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        street_cons ={
            1:[1,1,0,0], #l, r, u,d
            2:[0,0,1,1],
            3:[1, 0, 0,1],
            4:[0,1,0,1],
            5:[1,0,1,0],
            6:[0,1,1,0]
        }


        q = deque([(0,0)])
        visited = set([0,0])
        dirs = [(0,-1), (0,1), (-1,0), (1,0)]
        n,m = len(grid), len(grid[0])
        
        while q:
            y,x = q.popleft()
            if y == n-1 and x == m-1:
                return True
            
            curr_con = grid[y][x]
            for i, (dy, dx) in enumerate(dirs):
                y_,x_ = dy+ y, dx + x
                
                if y_ < 0 or y_> n-1 or x_ < 0 or x_ > m-1 or (y_, x_) in visited:
                    continue
                
                if not street_cons[curr_con][i]:
                    continue
                
                next_con = grid[y_][x_]
                opp_dir = i ^ 1
                if not street_cons[next_con][opp_dir]:
                    continue
                
                visited.add((y_,x_))
                q.append((y_,x_))
        return False
