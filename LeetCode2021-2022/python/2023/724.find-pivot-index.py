#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Strategy 1: prefix sum 
        Runtime:O(n)
        Space:O(1)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: the pivot point which balance the left side and the right side
        """
        total = sum(nums)
        prefixSum = 0
        for i, x in enumerate(nums):
            if prefixSum == total - prefixSum - x:
                return i
            prefixSum += x
        return -1

# @lc code=end
