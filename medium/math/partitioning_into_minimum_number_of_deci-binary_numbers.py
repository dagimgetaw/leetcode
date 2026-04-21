class Solution:
    def minPartitions(self, n: str) -> int:
        arr = list(n)
        num = [int(x) for x in arr]
        
        return max(num)
                