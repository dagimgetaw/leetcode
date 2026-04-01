class Solution:
    def maxDepth(self, s: str) -> int:
        current = 0
        max_depth = 0
        
        for c in s:
            if c == '(':
                current += 1
                max_depth = max(max_depth, current)
            elif c == ')':
                current -= 1
        
        return max_depth
        