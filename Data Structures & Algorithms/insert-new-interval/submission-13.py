class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 0 1 1 0 1 1 0 
        # 0 1 2 1 1 1 0
        # don't naiively just do a number line approach.
        # use the fact that the intervals are given to us in sorted order.
        # loop thru the sorted intervals.
        # compare target left with current range.
        # if target left is inside of this range, we need to overlap.
        # figure out which intervals overlap with the right pointer
        # and combine.
        # if target left is below this range, we must insert it here. count
        # where target right overlaps
        # just keep track of last overlapping for the right side?
        if len(intervals) == 0:
            return [newInterval]
        def isOverlap(curr):
            return (newInterval[0] >= curr[0] and newInterval[0] <= curr[1]) or (newInterval[1] >= curr[0] and newInterval[1] <= curr[1]) or (newInterval[0] <= curr[0] and newInterval[1] >= curr[1]) or (newInterval[0] >= curr[0] and newInterval[1] <= curr[1])
            
        out = []

        # at each step, check if it is overlap. 
        # if not, add to the out
        # if it is, we need to while loop to see while it is an interval
        # maybe just use a while loop overall
        overlapping_l = newInterval[0]
        overlapping_r = newInterval[1]


        idx = 0

        index_to_insert = -1
        while idx < len(intervals):
            if isOverlap(intervals[idx]):
                
                overlapping_l = min(overlapping_l, intervals[idx][0])
                overlapping_r = max(overlapping_r, intervals[idx][1])
                print("Overlapping interval: ", (overlapping_l, overlapping_r))
                if index_to_insert == -1:
                    index_to_insert = idx
                
            else:
                out.append(intervals[idx])

            idx+=1

        

            
        if index_to_insert == -1:
            # locate the place to insert it
            # this means that our left is > prev[1] and right < curr[0]
            for i in range(1, len(out)):
                if overlapping_l > out[i-1][1] and overlapping_r < out[i][0]:
                    index_to_insert = i
                    break
        print(index_to_insert)

        
        if index_to_insert == -1:
            if overlapping_l < out[0][0]:
                index_to_insert = 0
            
            if overlapping_l > out[-1][0]:
                index_to_insert = len(out)
        
        out.insert(index_to_insert, [overlapping_l, overlapping_r])
        return out
        
            
        
        