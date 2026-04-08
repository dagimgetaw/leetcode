class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7

        for querie in queries:
            start, end, step, mul = querie

            i = start
            while i <= end:
                nums[i] = (nums[i] * mul) % MOD
                i += step

        result = 0
        for num in nums:
            result ^= num

        return result
        