class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0 
        n = len(nums)
        for i in range(n):
            nums[i] += prev
            prev = nums[i]
        return nums
             

