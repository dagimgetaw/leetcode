class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            value = min(height[left], height[right])
            value *= right - left
            ans = max(value, ans)
            
            if height[left] < height[right]:
                left += 1
            else:           
                right -= 1

        return ans
        