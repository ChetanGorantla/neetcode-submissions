class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at each step we need to either include a character from a or include a character from b
        # to reach s3
        # based on the current index, it must be either the character at index of a or index of b
        # so based on whichever one it is, update the pointer
        # and if both are equal, maybe explore by switching both pointers and seeing if either of them
        # are true?
        
        # memoize based on i and j, store whether or not we can interleave the remaining string?

        memo = {}

        if len(s3) > len(s1) + len(s2):
            return False

        def search(i, j, k):
            # if we've reached the end of our lookup then we're done
            if k == len(s3) and i == len(s1) and j == len(s2):
                return True

            # if we haven't reached the end of our lookup but we reached the end of one of our pointers
            # we need to check if the remaining of the pointers is equal to the remaining of s3

            # if reached the end of s1, then check if the remaining of s2 is equal to remaining of s3
            if i == len(s1):
                return s2[j:] == s3[k:]
            
            if j == len(s2):
                return s1[i:] == s3[k:]
            
            if k == len(s3):
                return False
            
            if (i,j) in memo:
                return memo[(i,j)]
            

            # we have not explored this pair of indices yet.
            # look at what s3[k] is
            left = s1[i]
            right = s2[j]
            target = s3[k]
            print(left, right, target)
            # check to see if both i and j equal to k
            located = False

            if left == target or right == target:
                # only right == target, shift pointers for j and k
                if left != target:
                    located = located or search(i, j+1, k+1)
                elif right != target:
                    located = located or search(i+1, j, k+1)
                else:
                    located = located or search(i, j+1, k+1) or search(i+1, j, k+1)
            
            memo[(i,j)] = located
            return located
        
        return search(0,0,0)
                    
            
