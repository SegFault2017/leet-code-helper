class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        in_degrees = {}
        
        for i in range(numCourses):
            in_degrees[i] = 0
        
        for to, at in prerequisites:
            g[at].append(to)
            in_degrees[to] +=1
        
        sources = []
        for course, d in in_degrees.items():
            if d ==0:
                sources.append(course)
        i = 0
        while sources:
            source = sources.pop()
            i +=1
            print(source) 
            for nextCourse in g[source]:
                in_degrees[nextCourse] -=1
                if in_degrees[nextCourse] == 0:
                    sources.append(nextCourse)
        return i == numCourses
            
            
        
