class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        
        prev_end = intervals[0][1]
        c = 0
        
        for start,end in intervals[1:]:
            if start<prev_end:
                c +=1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return c