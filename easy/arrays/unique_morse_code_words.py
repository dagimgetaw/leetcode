class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mores = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mores_word = set()
        
        for word in words:
            arr = []
            for char in word:
                arr.append(mores[ord(char) - 97])
            mores_word.add("".join(arr))
            
        return len(mores_word)
            