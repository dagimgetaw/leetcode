class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
                continue
            
            temp = num
            count = 0
            while temp & 1:
                count += 1
                temp >>= 1
            
            ans.append(num - (1 << (count - 1)))
        
        return ans
    