class Solution:
    def convertDateToBinary(self, date: str) -> str:
        from datetime import datetime
        date_object = datetime.strptime(date, "%Y-%m-%d")

        year = date_object.year
        month = date_object.month
        day = date_object.day
        
        output = ""
        output += str(bin(year)[2:])
        output += "-"
        output += str(bin(month)[2:])
        output += "-"
        output += str(bin(day)[2:])
        
        return output
    
    
date = "2080-02-29"
sol  = Solution()
print(sol.convertDateToBinary(date))