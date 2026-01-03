class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in range(len(arr)):
            arr.insert(index[i],  nums[i])
            
        return arr[:len(nums)]
        