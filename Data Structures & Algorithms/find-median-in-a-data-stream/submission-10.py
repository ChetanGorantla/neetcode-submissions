class MedianFinder:
    # maintain a minheap and maxheap that stores the middle value
    # take the min + max / 2 and return that
    # if odd length min == max, proper calculation
    # if even length proper calculation

    # maintain the size of both
    # the size can't exceed total elements / 2
    # the minheap needs to store the second half of the list
    # the maxheap needs to store the first half of the list
    # if the new entry is greater than the current second half min,
    # pop from the second half and add to the lower half
    # add the new value to the upper half
    # when findmedian is called we need to peek both and add and divide and return

    def __init__(self):
        self.upper = []
        self.lower = []
        self.size = 0

    def addNum(self, num: int) -> None:
        
        if not (self.upper and self.lower):
            self.upper.append(num)
            self.lower.append(-1 * num)
            self.size+=1
            return
        cmp = self.upper[0]

        # if the current size is odd, we need to duplicate the value
        # instead of popping

        if num >= cmp:
            # shift to the right
            if self.size % 2 == 1:
                heapq.heappop(self.upper)
                heapq.heappush(self.upper, num)
                
                
            else:
                
                heapq.heappush(self.upper, num)
                heapq.heappush(self.lower, -1 * self.upper[0])
                
            
        else:
            # num < cmp
            # remove from lower and add to upper
            if self.size % 2 == 1:
                #popped = heapq.heappop(self.upper)
                heapq.heappop(self.lower)
                heapq.heappush(self.lower, -1 * num)
                
                
            else:
                heapq.heappush(self.lower, -1 * num)
                heapq.heappush(self.upper, -1 * self.lower[0])


        self.size+=1
        print(str(self.lower) + " " + str(self.upper))

    def findMedian(self) -> float:
        
        return (self.upper[0] + (-1 * self.lower[0]))/2;
        