class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # at each step from 0 to k or while we have options to choose
        # from (all options could have higher capital requirements, forcing an exit

        # we need to look at our current capital and pull unvisited projects with capital <= currcapital
        # (populate a maxheap with (profit, capital)) where all capital meets our threshold requirement.
        # so maybe sort by capital by zipping profits and capital
        # and maintain an index within capital for our index to
        # start looking for more candidates from when we've finished
        # a step


        combined = sorted(zip(capital, profits))
        capital, profits = zip(*combined)
        # just append based on profits
        candidates = []

        
        # based on our current capital, populate our candidates
        # in maxheap insertion order based on indices where capital[i] <= currcapital

        # at the end we need to update candidates
        i = 0
        ind = 0
        n = len(profits)
        currcapital = w
        # initially populate candidates based on w

        while i < k:
            # populate the heap based on our current capital
            while ind < n and capital[ind] <= currcapital:
                heapq.heappush(candidates, -profits[ind])
                ind+=1
            
            # if no poll candidate, return currcapital
            if not candidates:
                return currcapital
            poll = -heapq.heappop(candidates)
            currcapital+=poll
            i+=1
        return currcapital
