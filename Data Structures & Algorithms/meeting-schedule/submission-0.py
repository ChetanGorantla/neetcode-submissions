"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # we need to make our own sorting algorithm
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        list.sort(intervals, key = lambda interval: (interval.start, interval.end))
        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True