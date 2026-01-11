class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols

        curr_index = 0
        right, down, left, up = cols-1, rows-1, 0, 0 
        result = []

        while curr_index < n:
            for col in range(left, right+1):
                result.append(matrix[up][col])
                curr_index+=1
            
            for row in range(up+1, down+1):
                result.append(matrix[row][right])
                curr_index+=1
            
            if up != down:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[down][col])
                    curr_index+=1

            if left != right:
                for row in range(down-1, up, -1):
                    result.append(matrix[row][left])
                    curr_index+=1
            up+=1
            down-=1
            left+=1
            right-=1
        return result
        
