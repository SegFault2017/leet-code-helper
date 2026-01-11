class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combina = []
        n = len(nums)
        def backTrack(x:int, p:List[int]) -> None:
            combina.append(p[:])
            
            for i in range(x,n):
                p.append(nums[i])
                backTrack(i+1, p)
                p.pop()
            return
        backTrack(0,[])
        return combina
