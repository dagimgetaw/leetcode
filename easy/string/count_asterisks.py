class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisk = 0
        is_on = True
        
        for c in s:
            if c == "*" and is_on:
                asterisk += 1
                
            if c == "|":
                is_on = not is_on
                
        return asterisk
        