class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) +1
        edges_count = [0] * n

        for u,v in edges:
            edges_count[u-1]+=1
            edges_count[v-1]+=1
        
        for i, count in enumerate(edges_count):
            if count == len(edges):
                return i+1
        
