#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def slidingWindows(self, s: str) -> int:
        """Strategy:2 silding window
        Runtime:O(2n) where n is the length of s. Visit every  i, j at most twice
        Space:O(1)

        Args:
            s (str): a string with any ascii charaters

        Returns:
            int: the longest length of substring of s with no repeated character
        """
        slow, fast, n, longest = 0, 0, len(s), 0
        chars = [0] * 128

        while fast < n:
            chars[ord(s[fast])] += 1

            while chars[ord(s[fast])] > 1:
                chars[ord(s[slow])] -= 1
                slow += 1

            longest = max(longest, fast - slow + 1)
            fast += 1

        return longest

    def optimized(self, s: str) -> int:
        """Stragtegy 2: Optimized
        Runtime:O(n) where n is the length of s. Visit every i,j at most once
        Space:O(1)
        Args:
            s (str): a string with any ascii characters

        Returns:
            int: [description]
        """
        longest, n, i = 0, len(s), 0
        idxes = {}
        for j in range(n):
            if(s[j] in idxes):
                i = max(i, idxes[s[j]])
            longest = max(longest, j - i + 1)
            idxes[s[j]] = j+1

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.optimized(s)
        # @lc code=end
