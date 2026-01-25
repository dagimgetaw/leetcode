class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        arr = []
        for n in nums:
            if n % 2 == 0:
                arr.insert(0, 0)
            else:
                arr.insert(len(arr), 1)

        return arr