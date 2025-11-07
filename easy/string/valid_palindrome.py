class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        txt = "".join([char for char in s if char.isalnum()])
        txt = txt.lower()

        return txt == txt[::-1]
        