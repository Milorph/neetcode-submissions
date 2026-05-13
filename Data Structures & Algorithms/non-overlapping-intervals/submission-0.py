class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < prev[1]:
                res += 1
                prev = [min(prev[0], intervals[i][0]), min(prev[1], intervals[i][1])]
            else:
                prev = intervals[i]

        return res 
