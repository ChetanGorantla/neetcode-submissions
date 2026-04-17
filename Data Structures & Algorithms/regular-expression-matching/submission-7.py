class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # at each step, compute if the current value is matching or is special
        # if the special is . then it is matching
        # if the special is * then we can choose to continue with either the actual character in p
        # or the expected character in s (explore both)

        # continue with a * again

        # if the current char is not special and doesn't match, then check if the next value is *
        # if it is, then disregard this mismatch. Skip s pointer by 1 and skip p pointer by 2.
        # if it is not, return false

        # 2d based memoization based on the index, and whether or not we are continuing a *?
        memo = {}

        # at each step we can choose to also NOT include this value to account for when we
        # move backwards with a *

        def search(i, j):
            if i == len(s):
                # loop to see if we can exhaust j more
                # otherwise return false
                while j + 1 < len(p) and p[j+1] == '*':
                    j+=2
                
                return j == len(p)
            
            if j == len(p):
                return False
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            actual = s[i]
            provided = p[j]

            # if the next value is a star, from i+1 until s[i] doesnt match p[j], increment i
            # and call search on that and also skip it (shift both pointers) to treat as a no count
            valid = False

            if j+1 < len(p) and p[j+1] == '*':
                # the next value is a star, we have the choices to skip or repeat a # of times
                valid = valid or search(i, j+2)
                while i < len(s) and (p[j] == '.' or s[i] == p[j]):
                    i+=1
                    valid = valid or search(i, j+2)
                    
            else:
                # if the next value is not a star, just process the current two as usual
                if actual == provided or p[j] == '.':
                    valid = valid or search(i+1, j+1)
                # if not matching then this is false
            
            memo[(i,j)] = valid
            return valid

        return search(0, 0)


