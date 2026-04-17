class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        hashset = set()
        l = 0
        for r in range(0,len(s)):
            hashset.add(s[r])
            print(hashset)
            print(s[l:r+1])
            
            if (len(hashset) != r-l+1):
                print("duplicate at ", r)
                
                print("length of set ", len(hashset))
                print("l to r ",  l, r)
                print("size of current substring", r-l+1)
                hashset.remove(s[l])
                
                l+=1
                if (s[l-1] in s[l:r+1]):
                    hashset.add(s[l-1])
                
            else:
                maxlen = max(maxlen, r-l+1)
                
        return maxlen
        