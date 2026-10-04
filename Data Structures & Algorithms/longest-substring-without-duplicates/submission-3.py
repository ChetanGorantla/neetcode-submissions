class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # extend the window until we encounter an instance in which 
        # we have a repeat
        # maintain a set
        # if we ever find a duplicate then reset the set

        window = set()
        # remove from the window until we don't havee the issue anymore
        maxlen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            
            window.add(s[r])
            maxlen = max(len(window), maxlen)
        
        return maxlen

        