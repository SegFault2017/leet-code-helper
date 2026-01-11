#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ returns an index of an element that matches target, Otherwise, 
        return insert position
        Runtime: O(n log(n))
        Space: O(1)

        Args:
            nums (List[int]): a list of integers
            target (int): an integer target

        Returns:
            int: an index
        """

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid +1
            else:
                hi = mid -1

        return lo

        
        
# @lc code=end

