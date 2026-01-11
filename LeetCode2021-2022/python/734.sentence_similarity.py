class Solution:
    from collections import defaultdict
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        s1_len = len(sentence1)
        s2_len = len(sentence2)
        similar = defaultdict()

        if s1_len != s2_len:
            return False

        
        for w1, w2 in similarPairs:
            similar[w1].add(w2)
            similar[w2].add(w1)
        
        for idx in range(s1_len):
            w1 = sentence1[i]
            w2 = sentence2[i]
            if w1 == w2 or w2 in similar[w1]:
                continue
            return False
        return True
            
            
