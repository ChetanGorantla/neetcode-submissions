class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = r = 0
        minimum_days = sys.maxsize
        for weight in weights:
            l = max(l, weight)
            r += weight
        
        while l <= r:
            m = math.ceil((l+r)/2)

            # loop through weights and compute each bucket
            curr_bucket = 0
            curr_days = 1
            for weight in weights:
                curr_bucket+=weight
                if curr_bucket > m:
                    curr_bucket = weight
                    curr_days+=1
                
            if curr_days <= days:
                # we have days to spare, make our capacity more strict
                r = m-1
                minimum_days = m
            else:
                # we spent more days than allocated, widen our capacity
                l = m+1
            

        return minimum_days
            