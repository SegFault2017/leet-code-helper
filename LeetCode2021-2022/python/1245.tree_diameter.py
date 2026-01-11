class Solution:
    from collections import defaultdict
    def topoBFS(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for at, to in edges:
            g[at].append(to)
            g[to].append(at)

        leaves = []
        for v, es in g.items():
            if len(es) == 1:
                leaves.append(v)

        layers = 0
        vertices = len(edges) - 1
        while vertices > 2:
            vertices -= len(leaves)
            layers+=1
            next_leaves = []
            for leaf in leaves:
                neigh = g[leaf].pop()
                g[neigh].remove(leaf)
                if g[neigh] == 1:
                    new_leaves.append(neigh)
           leaves = new_leaves 
        return layers + 2 * (0 if vertices == 1 else 1)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        ##return self.topoBFS(edges)
        
        ## DFS
        diameter = 0
        visited = [False] * (len(edges) + 1) 
        g = defaultdict(list)
        
        for at, to in edges:
            g[at].append(to)
            g[to].append(at)

        def dfs(node) -> int:
            nonelocal diameter
            
            visited[node] = True
            
            longest1, longest2 = 0,0
            distance = 0
            for neigh in g[node]:
                if not visited[neigh]:
                    distance = dfs(neigh) + 1
                if distance > longest_1:
                    longest_1, longest_2 = distance, longest_1
                else distance > longest_2:
                    longest_2 = distance
                
            diameter = max(diameter, longest_1 + longest_2)
            return longest_1
        dfs(0)
        return diameter
            
            
                    
            

