class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        rev=str(x)[::-1]

        if int(rev) == x:
            return True
        else:
            return False
    
    