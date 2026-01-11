#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """search perform a binary search on nums, return an index of an element
        that matches target,other wise -1
        
        Strategy 1: Binary Search
        Runtime:O(n log(n))
        Space: O(1)


        Args:
            nums (List[int]): a list of integers 
            target (int): the target value

        Returns:
            int: an index
        """

        lo = 0
        hi = len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if(nums[mid] == target):
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid -1
        return -1
            
        
# @lc code=end

