class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # should we have a priority queue of values?
        # maintain a hashmap of frequencies as well
        # when we expand and compress, update the frequency hashmap
        # at each step, we need to figure out what our max value is
        # to do so, get the top of our priority queue. if it's not valid anymore
        # (not exist in hashmap anymore (freq == 0)) then pop it out and try the next candidate
        # when we compress, if the decremented freq is 0, delete the key
        # instead of deleting keys we can just make a defaultdict and say not map[key]
        if k == 1:
            return nums

        window = defaultdict(int)
        heap = []
        r = -1
        out = []
        for l in range(0, len(nums)-k+1):
            
            # expand our window
            while r-l+1<k:
                r+=1
                # consume this value
                # if this is the first time we're seeing this value, then 
                # add it to our heap
                if not window[nums[r]]:
                    heapq.heappush(heap, -nums[r])
                window[nums[r]]+=1
                
            # compute what our max value is
            while not window[-heap[0]]:
                heapq.heappop(heap)
            
            maxval = -heap[0]
            out.append(maxval)
            #print(l, r, heap)
            # compress our window
            window[nums[l]]-=1
            l+=1
        
        return out