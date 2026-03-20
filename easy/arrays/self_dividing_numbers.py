class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for num in range(left, right + 1):
            if num <= 9:
                arr.append(num)
            else:
                interation = 0
                for n in str(num):
                    n = int(n)
                    if n == 0:
                        break
                    
                    if num % n == 0:
                        interation += 1
                
                if interation == len(str(num)):
                    arr.append(int(num))
                    
        return arr
        