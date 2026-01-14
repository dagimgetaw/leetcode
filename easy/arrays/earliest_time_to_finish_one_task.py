class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        time = tasks[0][0] + tasks[0][1]
        for arr in tasks:
            time = min(time, arr[0] + arr[1])

        return time
    