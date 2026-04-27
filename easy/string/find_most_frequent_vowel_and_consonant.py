class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0] * 26
        max_vowel, max_conso = 0, 0

        for c in s:
            i = ord(c) - ord('a')
            freq[i] += 1
            if c in 'aeiou':
                max_vowel = max(max_vowel, freq[i])
            else:
                max_conso = max(max_conso, freq[i])

        return max_vowel + max_conso
        
        