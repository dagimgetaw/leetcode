class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num = min(nums)
        operation = 0
        
        while num < k:
            operation += 1
            nums.remove(num)
            num = min(nums)
        
        return operation
        