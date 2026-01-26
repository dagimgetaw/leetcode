class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # option one with O(N * M) complexity 5% beats
        tartget = list(allowed)
        arr = []
        count = 0
        
        for word in words:
            arr.append(set(list(word)))
                
        for word in arr:
            length = len(word)
            temp = 0
            for c in word:
                if c in tartget:
                    temp += 1
                    
            if temp == length:
                count += 1
                
        return count
        
        # option two with O(N) complexity 100% beats
        count = 0
        target = set(allowed)
        
        for word in words:
            if target.issuperset(word):
                count += 1
                
        return count
            
            