class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create a frequency map
        # for each character, if the character count is not zero, we must add
        # this into a queue and decrement its count
        # once you find a charactrr you have to loop as many times as it takes
        # until you have exhausted everything in the queue

        # maybe instead of a frequency map we maintain a map of the last index
        # of a specific character?
        # and we have to travel and add those to a queue
        # and at each step we need to poll from the queue, and travel
        # that distance in the array
        # keep a boolean tracker of whether or not we are pursuing an index
        
        sizes = []

        queue = deque()
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        # now that we're done populating our frequency map, we can go ahead and 
        # use our queue
        idx = 0
        maxind = 0
        l = 0
        while idx < len(s):
            # get the current value
            curr = s[idx]
            ending = last[curr]

            maxind = max(maxind, ending)
            print(maxind)
            # we need to continue looping to maxind
            if idx == maxind:
                # we are done with this substring
                # add the size
                sizes.append(maxind-l+1)
                l = idx+1
                maxind = l
            
            idx+=1
        return sizes