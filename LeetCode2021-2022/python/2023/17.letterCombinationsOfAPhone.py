class Solution:
    from collections import defaultdict
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        table = defaultdict(list)
        table['2'] = ['a', 'b', 'c']
        table['3'] = ['d', 'e', 'f']        
        table['4'] = ['g', 'h', 'i']        
        table['5'] = ['j', 'k', 'l']        
        table['6'] = ['m', 'n', 'o']        
        table['7'] = ['p', 'q', 'r', 's']        
        table['8'] = ['t', 'u', 'v']        
        table['9'] = ['w', 'x', 'y', 'z']
        
        combina = [];
        def backTrack(x:int, p:str) -> None:
            if x == n:
                combina.append(p)
                return
            
            for alpha in table[digits[x]]:
                backTrack(x+1, p + alpha)
            return
        backTrack(0, "")
        return combina
