#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """ Strategy1: Groupping
        Runtime: O(n)
        Space: O(1)

        Args:
            s (str): the target string

        Returns:
            int: maimum# of contigious of same 0's and 1's block
        """

        result = 0
        count = 1
        group = []

        n = len(s)
        for i in range(1, n):
            if s[i] != s[i-1]:
                group.append(count)
                count = 1
            else:
                count += 1

        group.append(count)

        n = len(group)
        for i in range(1, n):
            result += min(group[i], group[i-1])

        return result

# @lc code=end
