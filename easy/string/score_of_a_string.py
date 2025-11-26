class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_value = []
        for c in s:
            ascii_value.append(ord(c))
            
        score = 0
        for i in range(len(ascii_value)-1):
            score += abs(ascii_value[i] - ascii_value[i+1])
        
        return score
        