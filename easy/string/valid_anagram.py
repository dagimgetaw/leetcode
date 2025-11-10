class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        print(set(s))
        
        x = "".join(sorted(s))
        y = "".join(sorted(t))
        
        return x == y
    
s = "hello"
t = "bello"
sol =Solution()
print(sol.isAnagram(s, t))