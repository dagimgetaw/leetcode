class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = nums[0]
        
        for num in nums:
            value = 0
            for n in str(num):
                value += int(n)
                
            ans = min(ans, value)
            
        return ans
        