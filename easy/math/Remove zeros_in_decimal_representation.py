class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n)
        res = s.replace("0", "")
                
        return int(res)
