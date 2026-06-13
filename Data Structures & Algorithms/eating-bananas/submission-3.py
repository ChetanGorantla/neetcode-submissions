class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the lowest l upon exiting
        # we are doing binary search over a range
        # and storing the pre-image as our result
        # at each iteration, loop through the array and count the # of hours needed at this rate 

        # our binary search space is our rate
        # if we are able to eat all, then shift window left
        # if we aren't able to eat all, then shift window right


        # what is the lowest rate? 1
        # what is the highest rate? the largest pile
        l = 1
        r = 0
        for pile in piles:
            r = max(r, pile)
        
        k = 0

        while l <= r:
            rate = (l+r)//2
            #print(rate)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            
            if hours <= h:
                r = rate - 1
                k = rate
            else:
                l = rate + 1
            
            # when have we found a successful entry?
            # when we are able to eat within the hours
            
            # if we aren't able to eat within the hours, we can't say anything about our rate.
        
        return k