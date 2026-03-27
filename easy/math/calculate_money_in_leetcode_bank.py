class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week_start = 1
        
        for i in range(n):
            total += week_start + (i % 7)
            
            if i % 7 == 6:
                week_start += 1
                
        return total
        