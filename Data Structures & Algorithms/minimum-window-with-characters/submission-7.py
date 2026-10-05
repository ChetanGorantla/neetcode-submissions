class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we need to shift towards the next value that contributes
        # value to our window, do the same when compressing

        # take on this value. if our unique fulfill count reaches our target, we've found
        # a window. now we need to compress the window. while the unique fulfill count is met,
        # we need to update our minimum window
        # the moment our unique fulfill count isn't met, we need to start shifting our r
        # to fulfill it.
        
        if len(t) > len(s):
            return ""
        
        l = 0
        
        

        have = defaultdict(int)
        need = defaultdict(int)
        for i in range(len(t)):
            need[t[i]]+=1
        remaining = len(need)
        minl = 0
        minlen = sys.maxsize
        for r in range(len(s)):
            # expand to add on the newest value
            have[s[r]]+=1
            # check to see if we've met a requirement
            if have[s[r]] == need[s[r]]:
                remaining-=1
            
            # now we need to compress the window while we're full
            while remaining == 0:
                # shift l
                # compute if we're at the best l
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minl = l
                
                # shift l
                have[s[l]]-=1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    remaining+=1
                l+=1
        
        return "" if minlen == sys.maxsize else s[minl:minl+minlen]
            
            
