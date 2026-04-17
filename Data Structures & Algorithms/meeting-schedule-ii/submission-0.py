"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we need to maintain a queue of intervals to be added
        # we need to peek at each interval that is overlapping
        # and check to see if these are overlapping
        # if so, pop that overlapping one from the queue as it has now
        # constituted towards an existing day
        # if not, keep it in the queue and add a new day.
        # what is inside of the queue in the first place?
        # the queue stores intervals that represent days
        # so i think we can actually just check the queue length at the end
        # instead of maintaining a count
        # for each interval, peek the queue and see if there's any overlap.
        # if there is, then create a new day (add to the queue)
        # if there is not, then pop and add to the queue (updating the day)
        # our queue needs to be priority based on the smallest possible
        # ending time

        list.sort(intervals, key = lambda interval: (interval.start, interval.end))
        for interval in intervals:
            print(f"{interval.start}, {interval.end}")
        queue = []
        for interval in intervals:
            if not queue:
                heapq.heappush(queue, (interval.end, interval.start))
            else:
                # peek from the queue
                recent = queue[0]
                if recent[0] > interval.start:
                    # there's an overlap
                    # we need to add this day to the queue
                    heapq.heappush(queue, (interval.end, interval.start))
                else:
                    #there's no overlap
                    # update this day
                    heapq.heappop(queue)
                    heapq.heappush(queue, (interval.end, interval.start))
        
        return len(queue)
            