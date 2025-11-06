class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = s.strip()
        m = n.split()
        return len(("").join(m[-1:]))
        