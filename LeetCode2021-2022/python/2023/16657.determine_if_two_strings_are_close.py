class Solution:
    from collections import Counter
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1_counter = Counter(word1)
        w2_counter = Counter(word2)
        
        for key in w1_counter:
            if key not in w2_counter:
                return False

        freq_lst1 = [freq for key, freq in w1_counter.items()].sort()
        freq_lst2 = [freq for key, freq in w2_counter.items()].sort()
        
        for i in range(freq_lst1):
            if freq_lst1[i] != freq_lst2[i]:
                return False
        return True
        -- INSERT --
