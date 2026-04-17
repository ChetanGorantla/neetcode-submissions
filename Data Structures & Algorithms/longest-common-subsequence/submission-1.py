class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # store memoized results based on index in text1 and index in text2?

        # let text1 represent the smaller string
        # let text2 represent the larger string

        # for each character in text1, we need to compute the longest subsequence for the rest
        # of text2
        # so at each index in text1, we decide whether or not to choose this character.
        # if we choose it, we need to 

        # store the indices of each character in the longer string inside a hashmap
        # when we call the method, access the indices, and perform the recursive call on
        # all of them (only explore indices that are greater than the current text2 index tho)
        
        memo = [[-1 for _ in range(len(text2))] for __ in range(len(text1))]


        # we want to store the length of the maximum common subsequence from this character till the 
        # end given i and j

        def search(i, j):
            # if i or j goes out of bounds, return 0
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            # we have not explored this.
            # there are 2 cases
            # either both characters are equal, or they are different
            # if they are both equal, we need to shift both pointers
            if text1[i] == text2[j]:
                memo[i][j] = 1 + search(i+1, j+1)
            else:
                # the characters are different
                # we need to explore the paths
                maximum = max(search(i+1, j), search(i, j+1))
                memo[i][j] = maximum
            
            return memo[i][j]
        

        return search(0,0)


    
