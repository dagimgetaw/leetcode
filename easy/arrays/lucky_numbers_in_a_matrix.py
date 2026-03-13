class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        arr = []
        
        for row in matrix:
            min_row = min(row)
            index = row.index(min_row)
            
            print(min_row, index)
            
        return matrix
    
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(Solution().luckyNumbers(matrix))