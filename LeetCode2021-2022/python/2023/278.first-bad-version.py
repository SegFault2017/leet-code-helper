#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        returns the first bad version of a release
        Runtime:O(n log(n)))
        Space:O(1)
        :type n: int
        :rtype: int
        """

        lo,hi = 0, n
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if(isBadVersion(mid)):
                hi = mid -1
            else:
                lo = mid+1
        return lo
        
# @lc code=end

