class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
		
        ctr = Counter(nums) 
        def check(n):
            return ctr[n]
        
        nums.sort(reverse=True)
        nums.sort(key=check)
        
        return nums
        