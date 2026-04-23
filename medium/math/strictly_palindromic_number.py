class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            temp = []
            x = n
            
            while x:
                x, remainder = divmod(x, base)
                temp.append(str(remainder))
            
            s = "".join(reversed(temp))
            
            if s != s[::-1]:
                return False
        
        return True 
        