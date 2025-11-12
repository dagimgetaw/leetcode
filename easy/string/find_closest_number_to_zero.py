class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        arr = [abs(n) for n in nums]
        
        s = min(arr)
        
        index = [i for i in range(len(arr)) if arr[i] == s]
        
        res = nums[index[0]]
        
        for n in index:
            res = max(res, nums[n])
        
        return res
