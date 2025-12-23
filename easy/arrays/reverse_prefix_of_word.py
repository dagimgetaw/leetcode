class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.find(ch) == -1: return word
        
        prefix = word[:word.find(ch)+1:]
        reversed_prefix = prefix[::-1] + word[word.find(ch)+1:]

        return reversed_prefix
