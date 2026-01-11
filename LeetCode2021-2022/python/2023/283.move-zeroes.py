#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Strategy 1: 2 Pointers
        Runtime: O(n)
        Space:O(1)
        """

        n, slow, fast = len(nums), 0, 0
        while slow < n and nums[slow] != 0:
            slow += 1
            fast += 1

        while fast < n:
            while fast < n and nums[fast] == 0:
                fast += 1

            if fast < n:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
                fast += 1
        return
        # @lc code=end
