class Solution:
    def finalString(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            if s[i] == "i":
                arr = arr[::-1]
            else:
                arr.append(s[i])
                
        return "".join(arr)
        