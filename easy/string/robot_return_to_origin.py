class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [0, 0]
        
        for dir in moves:
            if dir == "L":
                origin[0] = origin[0] + 1
            elif dir == "R":
                origin[0] = origin[0] - 1
            elif dir == "U":
                origin[1] = origin[1] + 1
            else:
                origin[1] = origin[1] - 1
                
        if origin == [0, 0]:
            return True
        else:
            return False
            