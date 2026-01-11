class Solution:
    from collections import defaultdict
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        in_degrees = defaultdict(int)
        ancestors_set = defaultdict(set)
        for i in range(n):
            in_degrees[i] = 0
        for at, to in edges:
            g[at].append(to)
            in_degrees[to] +=1
            ancestors_set[to].add(at)
            
        sources =[]
        
        for node, deg in in_degrees.items():
            if deg == 0:
                sources.append(node)
        
        output = []
        while sources:
            source = sources.pop()
            for neigh in g[source]:
                ancestors_set[neigh] = ancestors_set[neigh] | ancestors_set[source]
                in_degrees[neigh] -=1
                if in_degrees[neigh] == 0:
                    sources.append(neigh)
        for i in range(n):
            output.append(sorted(ancestors_set[i]))
        
        return output
