class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not s or not goal: return False
        if len(s) != len(goal): return False
        if s == goal: return True
        
        n = 1
        while n < len(s):
            rotate_string = s[n:] + s[:n]
            if rotate_string == goal: return True
            else: n += 1

        return False
        