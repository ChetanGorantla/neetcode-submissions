class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 0
        r = 0
        for weight in weights:
            l = max(l, weight)
            r+=weight
        
        # lower and upper bound initialized
        # converge onto our minimum valid capacity
        min_cap = r
        while (l <= r):
            m = (l+r)//2
            print(m)
            # loop through the array to see if we can fit within our given days
            # is there a case when we don't need to check if it fits within given days?
            # no; we always need to check
            curr_days = 1
            curr_count = 0
            
            for weight in weights:
                curr_count += weight
                if curr_count > m:
                    curr_count = weight
                    curr_days += 1
            print(curr_days)
            if curr_days <= days:
                # shift left
                r = m-1
                min_cap = min(min_cap, m)
                # otherwise shift right, not valid solution
            else:
                l = m+1
        
        return min_cap
        