class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = list(boxes)
        box = []

        for i in range(len(arr)):
            num = 0  
            for j in range(len(arr)):
                if arr[j] == "1":
                        num += abs(j - i)
            box.append(num)

        return box
