class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        value = 0
        
        char = ord(coordinates[0]) - 96
        num = int(coordinates[1])
        
        value += char
        value += num
        
        if value % 2 == 0:
            return False
        else: 
            return True
            