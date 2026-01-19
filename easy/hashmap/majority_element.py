class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        
        counter = Counter(nums)
        majority = sorted(counter.items(), key=lambda item: item[1])
        
        return majority[len(majority)-1][0]
        