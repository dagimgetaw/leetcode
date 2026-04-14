class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num1 = bin(x)[2:]
        num2 = bin(y)[2:]
        
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        difference = 0
        
        for i in range(max_len):
            if num1[i] != num2[i]:
                difference += 1
                
        return difference
            