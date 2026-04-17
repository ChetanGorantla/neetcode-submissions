class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # define a function to check if two intervals are overlapping
        # maintain a current tracker of the left and right value to
        # append to the output list
        # initialize the [a,b] to be the 0th interval
        # after finding an overlapping interval, update a,b and continue the search
        # if not overlapping, append the current result if not empty and 
        # reset [a,b] to be empty
        # and continue along the search
        if not intervals:
            return [[]]


        list.sort(intervals)
        print(intervals)
        out = []
        curr = intervals[0]

        def isOverlapping(one, two):
            a1, b1, a2, b2 = one[0], one[1], two[0], two[1]
            # can actually be simplified if sorted
            return (a2 <= b1)
            #return (a1 <= a2 and b1 >= b2) or (a2 >= a1 and b2 <= b1) or (a1 >= a2 and a1 <= b2) or (b1 >= a2 and b1 <= b2)
                

        for i in range(1, len(intervals)):
            if isOverlapping(curr, intervals[i]):
                print(f"{curr} overlapping {intervals[i]}")
                curr[0] = min(curr[0], intervals[i][0])
                curr[1] = max(curr[1], intervals[i][1])
            else:
                out.append(curr)
                curr = intervals[i]
        out.append(curr)
        return out