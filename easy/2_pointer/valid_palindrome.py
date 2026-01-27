class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        arr = []
        for c in s:
            if c.isalnum():
                arr.append(c.lower())
                
        x, y = 0, len(arr) - 1
        while x <= y:
            if arr[x] != arr[y]:
                return False
            x += 1
            y -= 1
            
        return True
        