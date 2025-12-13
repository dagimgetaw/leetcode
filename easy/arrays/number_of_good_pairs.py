class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        i, j = 0, 1
        while i != len(nums) - 1:
            if nums[i] == nums[j] and i < j: count += 1
            
            j += 1
            if j  == len(nums): 
                i += 1
                j = i + 1
        
        return count
