class Solution:
    def rowColCounting(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        rowCount, colCount = [0]*n, [0]*m
        
        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    rowCount[i] +=1
                    colCount[j] +=1
        
        count = 0
        for i in range(n):
            for j in range(m):
                count += picture[i][j] == 1 and rowCount[i] == 1 \
                                            and colCount[j] == 1:
        return count
    def rowColCountingSmall(self, picture: List[List[str]]) -> int:
        return 0

    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        return 
                
                    
        
