class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # store the smaller string
        # store the larger string

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        # text1 is smaller than text2
        memo = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            # we want to explore this option
            if (i,j) in memo:
                return memo[(i,j)]
            
            # we have not explored this option
            # we need to see if the current characters are equivalent
            maxlen = 0
            if text1[i] == text2[j]:
                maxlen = 1 + dfs(i+1, j+1)
            else:
                # we can shift either one
                maxlen = max(dfs(i+1, j), dfs(i, j+1))
            memo[(i,j)] = maxlen
            return maxlen

        return dfs(0,0)