class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # at each step store this memoized result as 1 + min(nothing, insert, delete, replace)

        # if this current value equals word2, return 0

        # store the index inside memo, and the value is the distance


        memo = {}

        # if the characters are different, then distance = 1 + min(insert, delete, replace)
        # otherwise distance = (nothing (shift pointers call))

        # if r reaches length of word2, we've finished the call so return 0
         
        def search(l, r):
            
            # if finished looking thru BOTH
            if l == len(word1) and r == len(word2):
                return 0

            # if l is out of bounds, we need to insert as many as we can from r
            if l >= len(word1):
                return len(word2) - r 
            
            # if r is out of bounds, we need to delete as many as we can from l
            if r >= len(word2):
                return len(word1) - l 
            
            if (l, r) in memo:
                return memo[(l, r)]

            
                
            # we have not explored this pair yet.

            # check to see if they're matching
            if l < len(word1) and r < len(word2) and word1[l] == word2[r]:
                # if matching, shift pointers
                distance = search(l+1, r+1)
            else:
                # if not matching, we need to operate on this index
                distance = 1 + min(search(l+1, r+1), min(search(l+1, r), search(l, r+1)))
                
            memo[(l,r)] = distance
            return distance
        
        return search(0,0)
                