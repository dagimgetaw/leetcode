class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        counter = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for c in balloon:
            res = min(res, counter[c] // balloon[c])
            
        return res
