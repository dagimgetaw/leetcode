class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num1 = bin(start)[2:]
        num2 = bin(goal)[2:] 
        max_len = max(len(num1), len(num2))

        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        step = 0
        
        for i in range(len(num1)-1, -1, -1):
            if num2[i] != num1[i]:
                step += 1
            
        return step
        