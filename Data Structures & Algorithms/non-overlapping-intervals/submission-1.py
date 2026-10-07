class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by starting time
        # we need to remove the intervals that overlap
        # maintain a stack of the intervals that exist
        

        # we can do this greedily by maintaining the minimum
        # of the end times if there's an overlap
        intervals.sort()

        prevend = -sys.maxsize
        c = 0
        for interval in intervals:

            if interval[0] >= prevend:
                prevend = interval[1]
            else:
                # there's an overlap
                prevend = min(prevend, interval[1])
                c+=1
        
        return c

