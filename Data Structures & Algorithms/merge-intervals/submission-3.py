class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        result = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > prev[1]:
                result.append(prev)
                prev = intervals[i]
            elif intervals[i][1] < prev[0]:
                result.append(intervals[i])
            else:
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]
        
        result.append(prev)

        return result