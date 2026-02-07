class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    result += 1

        return result
    
nums = [-1,1,2,3,1]
target = 2
print(Solution().countPairs(nums, target))