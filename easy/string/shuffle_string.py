class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        arr = [""] * len(s)
        
        for index, char in enumerate(s):
            arr[indices[index]] = char
                    
        return "".join(arr)
    
    
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol = Solution()
print(sol.restoreString(s, indices)) 