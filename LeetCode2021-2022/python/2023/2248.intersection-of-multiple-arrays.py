class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = {}
        result = []
        for sub in nums:
            for x in sub:
                if not x in freq:
                    freq[x] = 1
                else:
                    freq[x] = freq[x] + 1

        for k, v in freq.items():
            if v == len(nums):
                result.append(k)
        result.sort()
        return result
