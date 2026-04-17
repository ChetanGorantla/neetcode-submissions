class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals and queries
        # add intervals to a min-heap while start values are <= query
        # store end values and sizes
        # remove elements from the heap while the top element's end value is 
        # less than the current query
        # to basically traverse backwards in our sorted order of intervals
        # result for the query is the top element's size if heap is non empty
        # otherwise it's -1

        # reset the heap for every query
        # actually if we're accessing queries in sorted order i don't think we
        # should reset the heap, we should just keep appending based on the
        # pointer
        mappings = {}
        list.sort(intervals)
        print(intervals)
        

        out = []
        minheap = []
        i = 0
        for q in sorted(queries):
            print(i)
            # add intervals to the pqueue while interval's left value is <= q
            # after that, remove from the front of pqueue while the right value
            # is < q
            # to get the smallest right value >= q
            while i < len(intervals) and intervals[i][0] <= q:
                #print("Appending " + str((intervals[i][1] - intervals[i][0] + 1, intervals[i][1])))
                heapq.heappush(minheap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            
            while minheap and minheap[0][1] < q:
                #print("Popping " + str(pqueue[0]))
                heapq.heappop(minheap)
                

            
            
            mappings[q] = -1 if not minheap else minheap[0][0]
            
        
        return [mappings[q] for q in queries]


