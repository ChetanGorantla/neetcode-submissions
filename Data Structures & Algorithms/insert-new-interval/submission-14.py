class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # maintain a stack
        

        # loop through the overall list until we find comparison_b > curr_a 
        # that indicates an overlap
        # if so, merge the two
        # and set curr to be the merged
        # look at the next value.
        # curr_b > comparison_a

        # [1, 3] [0, 4]
        # [1, 2] [0, 3]
        # [1, 2] [2, 3]
        # [2, 4] [0, 3]
        # [3, 4] [0, 2]

        out = []

        # three cases. our new interval is completely before curr, completely after, or overlapping
        for i in range(len(intervals)):
            curr = intervals[i]
            if newInterval[1] < curr[0]:
                # completely before
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > curr[1]:
                # completely after
                out.append(curr)
            else:
                # there is some overlap, so merge the two
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])
            
        out.append(newInterval)
        return out
                    
        