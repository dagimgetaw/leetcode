class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(n ** 0.5) + 1

        from collections import defaultdict
        groups = defaultdict(list)

        for l, r, k, v in queries:
            if k > B:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k
            else:
                groups[(k, l % k)].append((l, r, v))

        for (k, rem), qs in groups.items():
            bucket = []
            for i in range(rem, n, k):
                bucket.append(i)

            m = len(bucket)

            diff = [1] * (m + 1)

            for l, r, v in qs:
                left = (l - rem) // k
                right = (r - rem) // k

                diff[left] = (diff[left] * v) % MOD
                if right + 1 < m:
                    diff[right + 1] = (diff[right + 1] * pow(v, MOD-2, MOD)) % MOD

            cur = 1
            for i in range(m):
                cur = (cur * diff[i]) % MOD
                nums[bucket[i]] = (nums[bucket[i]] * cur) % MOD

        res = 0
        for num in nums:
            res ^= num

        return res
        