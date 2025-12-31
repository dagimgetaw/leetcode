class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [0]
        
        leftSum, rightSum = [], []
        for i in range(len(nums)):
            leftSum.append(sum(nums[:i]))
            rightSum.append(sum(nums[i+1:]))
            
        arr = []
        for i in range(len(leftSum)):
            arr.append(abs(leftSum[i] - rightSum[i]))
            
        return arr
