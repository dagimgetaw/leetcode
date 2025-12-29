class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        x, y, z = 0, 1, 2
        count = 0
        
        process = True
        while process:
            if abs(arr[x] - arr[y]) <= a and abs(arr[y] - arr[z]) <= b and abs(arr[x] - arr[z]) <= c: count += 1
            
            z += 1
            if z == len(arr):
                y += 1
                z = y + 1
            if y + 1 == len(arr):
                x += 1
                y = x + 1
                z = y + 1
            if x + 2 == len(arr):
                process = False
                
        return count
        