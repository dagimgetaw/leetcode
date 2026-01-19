class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        
        counter = Counter(s)
        tar = Counter(target)
        
        res = len(s)
        for c in tar:
            res = min(res, counter[c] // tar[c])
            
        return res
        