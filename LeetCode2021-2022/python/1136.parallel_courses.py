class Solution:
    from collections import defaultdict 
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        in_degrees = defaultdict(int)
        
        for prev, course in relations:
            g[prev].append(course)
            in_degrees[course] +=1
        
        q =[]
        for i in range(1, n+1):
            if in_degrees[i] == 0:
                q.append(i)
        if not q:
            return -1
        semesters = 0
        leaves = 0
        while q:
            n = len(q)
            leaves +=n
            semesters +=1
            for _ in range(n):
                course = q.pop(0)
                for to in g[course]:
                    in_degrees[to] -=1
                    if in_degrees[to] ==0:
                        q.append(to)
        
        return semesters if leaves != n else -1
                    
            
        
        
        
