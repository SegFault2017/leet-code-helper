#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter  = Counter(s)
        longest = 0
        has_odd = False
        
        
        for _,v in counter.items():
            if v % 2 == 0:
                longest += v
            else:
                has_odd = True
                longest += v -1
        
        if has_odd:
            return longest +1
        
        return longest
        
        
# @lc code=end

