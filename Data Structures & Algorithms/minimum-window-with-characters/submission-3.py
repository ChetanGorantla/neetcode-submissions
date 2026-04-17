class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1+countT.get(c,0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity") #res is arbitrary, resLen is Integer.MAX_VALUE
        l = 0
        for r in range(len(s)):#loop thru each index of the string
            c = s[r] #c is current character
            window[c] = 1 + window.get(c,0) #updating the window

            if c in countT and window[c] == countT[c]: #if we match a target character in both hashmaps
                have += 1

            while have == need: #while all conditions met
                if (r-l+1) < resLen: #if our current length is a new minimum
                    res = [l,r]
                    resLen = (r-l+1)
                window[s[l]]-=1 #decrement count for first character of window
                if s[l] in countT and window[s[l]] < countT[s[l]]: #if we have lost our condition satisfaction after decrementing window count
                    have -=1
                l+=1 #increase l because we decremented count for first character (we shift upwards)
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            

        