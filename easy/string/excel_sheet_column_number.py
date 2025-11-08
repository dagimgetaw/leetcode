class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
            import math

            arr=[]
            res=0

            for char in columnTitle[::-1]:
                arr.append(ord(char)-64)

            for i in range(len(arr)):
                if i == 0:
                    res += arr[i]
                else:
                    res += math.pow(26, i) * arr[i]

            return math.floor(res)
