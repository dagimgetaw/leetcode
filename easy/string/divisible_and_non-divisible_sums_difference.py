class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr = list(range(1, n+1))
        
        diviseable, not_diviseable = 0, 0
        for num in arr:
            if num % m == 0: diviseable += num
            else: not_diviseable += num
            
        return not_diviseable - diviseable
        