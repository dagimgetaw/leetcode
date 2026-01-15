class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0
        length = len(arr)
        
        for i in range(length + 1):
            if i % 2 != 0:
                for j in range(0, length - i + 1):
                    count += sum(arr[j:j + i])
        
        return count
        