class Solution:
    from collections import defaultdict
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        in_degrees = defaultdict(int)
        
        for i, neighs in enumerate(graph):
            if not neighs:
                in_degrees[i] = 0
            for neigh in neighs:
                g[neigh].append(i)
                in_degrees[i] +=1
                
        sources =[]
        for node,degree in in_degrees.items():
            if degree == 0:
                sources.append(node)
        safes = [False] * len(graph)
        while sources:
            source = sources.pop()
            safes[source]^=1
            for neigh in g[source]:
                in_degrees[neigh]-=1
                if in_degrees[neigh] == 0:
                    sources.append(neigh)
        
        return [i for i, is_safe in enumerate(safes) if is_safe ]
        
        
       
