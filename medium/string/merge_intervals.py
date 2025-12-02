class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged_intervals = [intervals[0]]
        
        for start, end in intervals[1:]:
            last = merged_intervals[-1][1]
            
            if start <= last: merged_intervals[-1][1] = max(last, end)
            else: merged_intervals.append([start, end])
            
        return merged_intervals
        