class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        for n in gain:
            arr.append(arr[len(arr) - 1] + n)

        return max(arr)
