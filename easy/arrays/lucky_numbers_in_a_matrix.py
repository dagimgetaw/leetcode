class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        
        for row in matrix:
            min_row = min(row)
            index = row.index(min_row)
            col_arr = []
            
            for col in matrix:
                col_arr.append(col[index])
                
            max_col = max(col_arr)
            
            if min_row == max_col:
                arr.append(min_row)
            
        return arr
        