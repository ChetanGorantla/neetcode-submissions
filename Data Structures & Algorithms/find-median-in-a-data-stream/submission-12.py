class MedianFinder:
    # maintain a maxheap for the lower half
    # and a minheap for the upper half
    # place into respective one at each point
    

    # when inserting, check to see if this element belongs in
    # lower or upper based on the heads
    # if it's in between, then put it in lower
    

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        lower = self.lower
        upper = self.upper
        # start off with the case that it's empty
        if len(lower) == len(upper) == 0:
            lower.append(-num)
        elif len(lower) == 1 and len(upper) == 0:
            # there's only one value. 
            lower_head = -lower[0]
            if num > lower_head:
                upper.append(num)
            else:
                upper.append(-lower.pop())
                lower.append(-num)
        else:
            # there are values in both
            # determine where this should live
            # if we've inserted and now our length diff is more than 1,
            # we need to shift
            # [1, 2] [3]
            lower_head = -lower[0]
            upper_head = upper[0]
            if num <= lower_head:
                heapq.heappush(lower, -num)
                # check to see if the length is too big
                if len(lower)-len(upper) > 1:
                    # pop and shift
                    shift = -heapq.heappop(lower)
                    heapq.heappush(upper, shift)
            else:
                # num should exist in upper
                heapq.heappush(upper, num)
                if len(upper)-len(lower) > 1:
                    shift = heapq.heappop(upper)
                    heapq.heappush(lower, -shift)
    def findMedian(self) -> float:
        # retrieve head from whichever has longer len
        # if both equal, take mean
        upper = self.upper
        lower = self.lower
        if len(upper) > len(lower):
            return float(upper[0])
        elif len(lower) > len(upper):
            return float(-lower[0])
        else:
            return float(upper[0] - lower[0])/2
        