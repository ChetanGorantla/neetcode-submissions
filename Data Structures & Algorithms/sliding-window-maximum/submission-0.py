class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a tracker of the current max values and their index
        # if we ever shift out of that index then we need to find a new max value
        # we can use a maxheap?
        # we need to pop maxheap values that are out of bounds
        # if we shift out of index of the maxheap highest then we need to keep
        # popping 
        # actually, if we encounter a value that is out of position,
        # we can just pop it and use the next one
        # because it is GUARANTEED that the next one will be in position
        # if we traverse one at a time

        heap = []

        out = []

        # initialize the first window
        for i in range(k-1):
            heapq.heappush(heap, (-1 * nums[i], i))
        
        for i in range(k-1, len(nums)):
            heapq.heappush(heap, (-1 * nums[i], i))
            # peek the current max value
            print(i)
            print(heap)
            maximum = heap[0]
            while maximum[1] < i-k+1:
                heapq.heappop(heap)
                maximum = heap[0]
            
            # maximum is set to the correct value now.
            # we need to shift pointers
            
            out.append(-1 * maximum[0])
        
        return out
            
            
