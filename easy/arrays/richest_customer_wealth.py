class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for arr in accounts:
            wealth = max(wealth, sum(arr))
            
        return wealth
        