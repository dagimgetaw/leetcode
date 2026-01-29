class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        res = []
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        res.reverse()
                    
        return res
    
nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))

# 100 - 16, 100 - 