class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        from typing import List

        n = len(nums)
        count = 0
        i, j, k = 0, 1, 2

        while i < n - 2 and j < n - 1 and k < n:
            d1 = nums[j] - nums[i]
            d2 = nums[k] - nums[j]

            if d1 == diff and d2 == diff:
                count += 1
                i += 1
                j += 1
                k += 1
            elif d1 < diff:
                j += 1
            elif d1 > diff:
                i += 1
            elif d2 < diff:
                k += 1
            else:
                j += 1

        return count
