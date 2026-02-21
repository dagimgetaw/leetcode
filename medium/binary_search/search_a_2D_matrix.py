class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for arr in matrix:
            if arr[0] > target:
                break
            
            if arr[0] <= target <= arr[-1]:
                left, right = 0, len(arr) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return True
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return False
        