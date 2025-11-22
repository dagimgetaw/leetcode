class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        r = Counter(ransomNote)
        m = Counter(magazine)
            
        for c in r:
            if r[c] > m[c]: return False
                    
        return True
        