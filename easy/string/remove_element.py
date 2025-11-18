class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        count = 0
        
        for i in range(len(nums)):
            if val != nums[i]:
                nums[count] = nums[i]
                count += 1
        
        return count
        