class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # expand and compress a current window

        # create replacements for each r expansion
        # we need to define a target value for the window
        # 

        # maintain a tracker window with the hashmap
        # track the highest frequency element
        # k = windowsize-highestfreq

        # shift left pointer while currk == k
        # at each step, consume the right pointer

        # how to determine the highest frequency element?
        # do we loop through the hashmap at each time?

        frequencies = defaultdict(int)

        l = 0
        highestfreq = 0
        maxwindow = 0
        for r in range(len(s)):
            # take on the addition
            frequencies[s[r]]+=1
            highestfreq = max(highestfreq, frequencies[s[r]])
            while (r-l+1-highestfreq > k):
                frequencies[s[l]]-=1
                l+=1
            
            #print(l, r, highestfreq)
            maxwindow = max(maxwindow, r-l+1)
        
        return maxwindow
        

                