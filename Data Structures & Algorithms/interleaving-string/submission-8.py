class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at each step, we have to make a decision of
        # which character to put at this index
        # if neither character can be put in at this moment, then return false
        # explore whichever character can be put in
        # memoize based on index in s1 and s2?
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def explore(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == len(s1) and j == len(s2):
                return True
            
            # we are not at the end and haven't explored this yet
            # we need to attempt to explore i or j, if in bounds and matches
            possible = False
            #print(i,j)
            if i < len(s1) and s1[i] == s3[i+j]:
                possible = possible or explore(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                possible = possible or explore(i, j+1)
            
            memo[(i,j)] = possible
            return possible
        
        return explore(0,0)