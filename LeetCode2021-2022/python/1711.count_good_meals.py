class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        freq = {}
        max_sum = 2* max(deliciousness) if deliciousness else 0
        powers_of_two = [2 ** i for i in range(22) if 2**i <= max_sum]
        result =0

        for food in deliciousness:
            for power in powers_of_two:
                complement = power - food
                if complement in freq:
                    result = (result + freq[complement]) % MOD
            freq[food] = freq.get(food, 0)+1
        return result
