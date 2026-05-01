class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        arr.append(pref[0])
        
        for i in range(len(pref)-1):
            arr.append(pref[i] ^ pref[i + 1])
            
        return arr
        