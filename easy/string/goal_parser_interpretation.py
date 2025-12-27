class Solution:
    def interpret(self, command: str) -> str:
        res = "" 
        
        i = 1
        while i <= len(command):
            if command[i - 1] == "G":
                res += "G"
                i += 1
            elif command[i - 1] == "(" and command[i] == ")":
                res += "o"
                i += 2
            else:
                res += "al"
                i += 4     
        
        return res
            