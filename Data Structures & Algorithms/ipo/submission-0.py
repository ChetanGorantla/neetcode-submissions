class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # is there every any instance where we want to choose less than k projects
        # given that all profits are greater than zero?
        # the only instance in which we would do that is if there are no more
        # projects that we can afford
        
        # at each step we want to see which projects we can afford
        # and from those we want to choose the project that gives us the most profit

        # edge case:
        # k = 2, w = 2
        # profit: [3, 2, 2], capital = [2, 1, 1]

        # k = 1, w = 2
        # profit: [1, 3], capital = [1, 2]

        # digest in sorted order of capital requirements
        # append to the heap based on profits
        # at each selection, pop from profits and add to the total

        n = len(profits)
        indices = list(range(n))
        indices.sort(key=lambda i: capital[i])
        
        maxprofit = []
        idx = 0
        # maintain our idx based on our current capital value as we make a new move

        for i in range(k):
            # populate our heap based on our capital
            while idx < n and capital[indices[idx]] <= w:
                heapq.heappush(maxprofit, -profits[indices[idx]])
                idx+=1
            
            # pop from our profits
            # first ensure there is profit to pop
            if not maxprofit:
                break
            
            # pop
            w+=-heapq.heappop(maxprofit)
        
        return w