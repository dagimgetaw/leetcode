class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letter = ""
        for word in words:
            letter += word[:1]
            
        return letter == s
        