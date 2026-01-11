class Solution:
    def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s

        if numRows ==1:
            return s
            
		n = len(s)
        sections = math.ceil(n / (2 * numRows -2))
        cols = sections * (numRows -1)

        matrix = [[''] * cols for _ in range(numRows)]
        curr_index = n
        curr_row = 0
        curr_col = 0
        curr_index = 0
        
        while curr_index < n:
            while curr_row < numRows and curr_index < n:
                matrix[curr_row][curr_col] = s[curr_index]
                curr_row +=1
                curr_index -=1
            
            curr_row -=2
            curr_col +=1
            
            while curr_row > 0 and curr_index < n:
                matrix[curr_row][curr_col] = s[curr_index]
                curr_row -=1
                curr_col +=1
                curr_index +=1

        answer =""
        
        for i in range(numRows):
            answer += "".join(matrix[i])
        return answer
        
