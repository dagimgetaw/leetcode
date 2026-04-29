class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        for mask in range(1 << n):
            curr = 0
            for i in range(n):
                if mask & (1 << i):
                    curr ^= nums[i]
            res += curr
        
        return res
        