class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations = sorted(citations)[::-1]
        
        for i in range(0, len(citations)):
            if citations[i] >= i+1: h += 1
            else: return h
                
        return h
        