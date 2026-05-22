class Solution:
    def reorganizeString(self, s: str) -> str:
        # always start with highest frequency first
        
        # we need to wait for one step before re-inserting values
        # into the maxheap
        
        # store in pairs of (freq, char)
        frequencies = {}
        for char in s:
            if char not in frequencies:
                frequencies[char] = 0
            frequencies[char]+=1
        
        queue = []
        for char in frequencies:
            queue.append((-frequencies[char], char))
        
        heapq.heapify(queue)

        # or sub this out for a counter
        order = []
        saved = None
        while len(queue) > 0:
            poll = heapq.heappop(queue)
            #print(poll)
            # re-insert saved
            # make saved the poll value
            if saved and -saved[0] > 0:
                heapq.heappush(queue, saved)

            # account for saved by putting this after we re-insert saved if exists
            if -poll[0] > 1 and len(queue) == 0:
                return ""
            # track polled char
            order.append(poll[1])
            # re-insert old value
            

            # decrement the frequency
            decremented = (poll[0]+1, poll[1])
            saved = decremented

        return "".join(order)
        