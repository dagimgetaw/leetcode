class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        bob, alice = 0, 0
        arr = []
        
        while len(nums) != 0:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
            
        return arr
    
nums = [2,5]
sol = Solution()
print(sol.numberGame(nums))