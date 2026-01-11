class Solution:
    from collections import defaultdict
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return [i for i in range(n)]
        g = defaultdict(list)

        for at, to in edges:
            g[at].append(to)
            g[to].append(at)

        leaves = []
        for v, es in g.items():
            if len(es) == 1:
                leaves.append(v)
        
        vertices = n
        while vertices >2:
            vertices -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neigh = g[leaf].pop()
                g[neigh].remove(leaf)
                if len(g[neigh]) == 1:
                    new_leaves.append(leaves)
            leaves.append(new_leaves)
        return leaves
        
