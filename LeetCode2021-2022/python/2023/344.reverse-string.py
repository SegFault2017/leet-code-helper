#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do ot return anything, modify s in -place instead.
        Strategy 1: 2 pointers
        Runtime: O(n)
        space: O(1)

        Args:
            s (List[str]): a reversed list of the given string list
        """

        lo, hi = 0, len(s)-1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return


# @lc code=end
