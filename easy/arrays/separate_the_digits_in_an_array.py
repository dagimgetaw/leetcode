class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            for n in str(num):
                arr.append(int(n))
                
        return arr
