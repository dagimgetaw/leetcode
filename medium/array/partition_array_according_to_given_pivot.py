class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        min_arr = []
        mid_arr = []
        
        for n in nums:
            if n < pivot:
                min_arr.append(n)
            elif n == pivot:
                mid_arr.insert(0, n)
            else:
                mid_arr.insert(len(mid_arr), n)
                
        arr = min_arr + mid_arr
                
        return arr
    