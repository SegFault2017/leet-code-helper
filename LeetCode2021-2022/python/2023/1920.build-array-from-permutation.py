#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """Strategy 1: Math trick
        Store multiple values in on value
        Runtime: O(n)
        Space: O(1)

        Args:
            nums (List[int]): a list of positive integers

        Returns:
            List[int]: a list of positive integers
        """

        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n

        for i in range(n):
            nums[i] = nums[i] // n
        return nums
# @lc code=end
