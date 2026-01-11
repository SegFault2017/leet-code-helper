#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter


class Solution:

    def matches(self, c1: Counter, c2: Counter) -> bool:
        """Determine whether one Counter is equal to the othe and assume they 
        both have the same length
        Runtime:O(n), where n is the length of c1
        Space:O(1)

        Args:
            c1 (Counter): Counter 1
            c2 (Counter): Counter 2

        Returns:
            bool: if c1 == c2
        """

        for character in c1.keys():
            if character not in c2 or c2[character] != c1[character]:
                return False

        return True

    def hashMap(self, s1: str, s2: str) -> bool:
        """Strategy 2 one string will be a permutation of another if both 
        strings contain the same characters and the same frequency of characters.
        Runtime: O(nlogn + (m -n)mlog(m)), where n is the length of s1, and m is 
        the length of s2. (Use HashMap)
        Space:O(max(n,m))

        Args:
            s1 (str): list of characters
            s2 (str): list of characters

        Returns:
            bool: determine whether the permutation of s1 is a substring of s2.
        """
        n, m = len(s1), len(s2)
        if(n > m):
            return False

        c1 = Counter(s1)
        for i in range(m - n + 1):
            c2 = Counter(s2[i: i+n])
            if self.matches(c1, c2):
                return True
        return False

    def sorting(self, s1: str, s2: str) -> bool:
        """ Strategy 1: one string will be a permutation of another if both 
        strings contain the same characters and the same frequency of characters.
        Runtime: O(nlogn + (m -n)mlog(m)), where n is the length of s1, and m is 
        the length of s2.
        Space:O(max(n,m))

        Args:
            s1 (str): list of characters
            s2 (str): list of characters

        Returns:
            bool: determine whether the permutation of s1 is a substring of s2.
        """

        n, m = len(s1), len(s2)
        if n > m:
            return False

        sorted_s1 = sorted(s1)
        for i in range(m-n+1):
            if sorted_s1 == sorted(s2[i:i+n]):
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.hashMap(s1, s2)

# @lc code=end
