class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we need to explore outwards
        longest = 0
        out = ""
        # first do l = r = i
        # then do l = i, r = i+1

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            old = longest
            longest = max(longest, r-l-1)
            if longest > old:
                out = s[l+1:r]
        
        for i in range(len(s)-1):
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            old = longest
            longest = max(longest, r-l-1)
            if longest > old:
                out = s[l+1:r]
        
        return out