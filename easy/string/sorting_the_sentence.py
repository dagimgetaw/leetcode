class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        arr = [""] * len(words)
        
        for w in words:
            arr[int(w[-1]) - 1] = w[:-1]

        return " ".join(arr)
