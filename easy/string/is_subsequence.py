class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        pointer = 0  
        
        for char in s:
            res = t.find(char, pointer)
            
            if res == -1:
                return False
            
            pointer = res + 1
        
        return True
        