class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        res = 0
        
        for i in range(n):
            arr.append(start + 2 * i)
            
        for n in arr:
            res = res ^ n      
               
        return res
        