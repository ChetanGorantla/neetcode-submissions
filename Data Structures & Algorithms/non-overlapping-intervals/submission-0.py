class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        list.sort(intervals)

        # do we not just count the number of total overlapping intervals?
        # since we're in sorted order, we just need to check if curr[1] > next[0]

        # actually we need to remove whichever between curr and prev has the larger 
        # b value
        # because that has higher impact on future interval overlaps
        # so we basically need to track a boolean array of whether or not
        # this interval still "exists"
        # and when we make a decision, we need to update our prev and curr
        # to whatever matches
        # if we have found an overlapping interval
        # we need to set whichever one extends the furthest as nonexistent
        # and put prev as whichever one was the other one
        # and put next as the next value in the array
        # if we have not found an overlapping interval, put prev in next's position
        # and increment next's position by 1
        count = 0
        l = 0
        r = 1
        while (r < len(intervals)):
            prev = intervals[l]
            curr = intervals[r]
            if (curr[0] < prev[1]):
                # there is an overlap
                # switch l and r
                if (curr[1] < prev[1]):
                    l = r
                r+=1
                count+=1
            else:
                # there is no overlap
                l = r
                r+=1


        return count