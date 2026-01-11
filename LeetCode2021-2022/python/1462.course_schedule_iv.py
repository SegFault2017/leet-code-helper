class Solution:
    from collections import defaultdict
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq2next = defaultdict(list)
        next2prepreq = defaultdict(set)
        in_degrees = defaultdict(int)
        
        for i in range(numCourses):
            in_degrees[i] = 0
            
        for at, to in prerequisites:
            prereq2next[at].append(to)
            next2prepreq[to].add(at)
            in_degrees[to] +=1
        
        sources = []
        for course, degree in in_degrees.items():
            if degree == 0:
                sources.append(course)
        
        while sources:
            source = sources.pop()
            for nextCourse in prereq2next[source]:
                next2prepreq[nextCourse] |= next2prepreq[source]
                in_degrees[nextCourse] -=1
                if in_degrees[nextCourse] == 0:
                    sources.append(nextCourse)
        
        output = []
        for at, to in queries:
            output.append(at in next2prepreq[to])
        return output
                
        
        
                
            
        
