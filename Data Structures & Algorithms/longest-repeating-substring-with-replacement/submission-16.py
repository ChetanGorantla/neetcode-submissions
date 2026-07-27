class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need to push out our window to the point where the length of unique characters
        # is greater than k
        # at that point we need to shift our window because this is no longer valid
        # we should shift to the point where our window is now valid
        # we need to shift l so that we remove what we left and add what we enter
        
        l = 0
        
        maxlen = 0

        # we need to get the counts of the characters
        window = [0] * 26
        for r in range(len(s)):
            # accept r into our window
            window[ord(s[r])-ord('A')]+=1
            print(window)
            # check to see if we exceeded our max window size
            # what determines if we've exceeded our max window size?
            # if we have more non-dominants than we have k
            # compute the sum of the non-dominants
            # this is the same as computing r-l+1 - max_freq
            # and seeing if that is greater than k
            # if it is, we need to shift our window until r-l+1-max_freq is not > k
            max_freq = max(window)
            
            while r-l+1-max_freq > k:
                # we need to shift our window
                window[ord(s[l])-ord('A')]-=1
                l+=1
                max_freq = max(window)


            print(l,r)
            maxlen = max(maxlen, r-l+1)
        return maxlen