class Solution:
    def partitionString(self, s: str) -> int:
        # i'm thinking we have to partition outside in
        # maintain a range
        # actually why is this not possible in a one-pass?
        # at each stage we maintain a window
        # whenever we encounter a duplicate we reset window and increment count
        c = 1
        window = set()
        for i in range(len(s)):
            if s[i] in window:
                window = set()
                c+=1
            window.add(s[i])
        
        return c
