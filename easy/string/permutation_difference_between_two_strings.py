class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i in range(len(s)):
            result += abs(s.index(s[i]) - t.index(s[i]))
            
        return result
        