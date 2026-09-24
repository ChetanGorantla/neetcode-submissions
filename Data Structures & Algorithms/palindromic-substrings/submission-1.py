class Solution:
    def countSubstrings(self, s: str) -> int:
        # at each index, go outwards for as long as we can

        c = 0

        def expand(l, r):
            num = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                num+=1
            
            return num
            

        for i in range(len(s)):
            c+=expand(i,i)+expand(i,i+1)
        return c