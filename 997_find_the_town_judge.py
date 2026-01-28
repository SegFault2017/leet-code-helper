class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1

        points = [0]  * n

        for u,v in trust:
            points[v-1] +=1
            points[u-1] -=1
        
        for i in range(n):
            if points[i] == n - 1:
                return i +1
        return -1
