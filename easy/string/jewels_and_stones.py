class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if not jewels or not stones: return 0
        
        from collections import Counter
        
        ctr = Counter(stones)
        jewels = set(jewels)
        
        count = 0
        for c in jewels:
            if c in ctr:
                count += ctr[c]
        
        return count
    