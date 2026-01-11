class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_size = len(p)
        s_size = len(s)

        if p_size > s_size:
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        for idx, alpha in enumerate(p):
            p_count[ord(alpha) - ord('a')] +=1

        result = []
        for idx, alpha in enumerate(s):
            s_count[ord(alpha) - ord('a')] +=1

            if idx > p_size:
                s_count[ord(s[idx - p_size]) - ord('a')] -=1

            if p_count == s_count:
                result.append(idx - p_size +1)
        return result
            
            
        
