class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # maintain a heap of (time, val)
        # and maintain a global variable time
        # this will track whether or not we can actually use an item at a certain time
        # track consecutives as well
        # if we can use this item at this time but we reach three consecutives, 
        # we can't use this. change its time to +2
        # and continue
        # at the end of each segment change our time to +1
        
        # track the global max segment so far
        # minheap by (-capacity, letter)
        # at each step, we have multiple cases
        # at the start, add back in cooldown if its not none
        # the consecutive so far for the front element is already 2, so we can't add it.
        # we need to set it as the cooldown element
        # else, we can add this element to the segment. increment its consecutive, update its
        # state (capacity)
        queue = [[-a, "a"], [-b, "b"], [-c, "c"]]
        consecutive = default_consecutive = {"a":0, "b":0, "c":0}
        
        heapq.heapify(queue)
        cooldown = []
        segment = []
        #i = 0
        while queue:

            #i+=1
            print(queue, cooldown, segment, consecutive)

            
            # heap is populated
            # poll front
            poll = heapq.heappop(queue)
            front_capacity = -poll[0]
            front_char = poll[1]
            if front_capacity == 0:
                continue
            # check to see consecutive
            # only populate cooldown element AFTER polling
            if cooldown:
                heapq.heappush(queue, cooldown)
                
                cooldown = []
            
            # this will add a third consecutive. this cannot occur.
            # put this in cooldown.
            if consecutive[front_char] == 2:
                print(f"putting {front_char} in cooldown")
                cooldown = [-front_capacity, front_char]
                consecutive[front_char] = 0
                continue
            # we need our state of the queue to be ready after every iteration
            # this means we can't defer to later

            # we can add this element
            # wipe the consecutives of other values
            held = consecutive[front_char]
            # reset consecutive
            consecutive["a"] = 0
            consecutive["b"] = 0
            consecutive["c"] = 0
            segment.append(front_char)
            consecutive[front_char] = held+1
            # only add it if there is capacity for it
            if front_capacity == 1:
                continue
            
            # there is capacity for it, so add it back to the heap
            heapq.heappush(queue, [-(front_capacity-1), front_char])
        return "".join(segment)
            