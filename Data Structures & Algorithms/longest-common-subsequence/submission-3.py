class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # longest common subsequence from i and j
        # at each step, we need to see if i == j. if so, shift both
        # if not, try shifting one
        # if we reach the end of either, return 0


        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == len(text1) or j == len(text2):
                return 0
            
            # we aren't at the end yet.
            total = 0
            if text1[i] == text2[j]:
                total = 1 + dfs(i+1, j+1)
            else:
                total = max(dfs(i+1, j), dfs(i, j+1))
            
            memo[(i,j)] = total
            return total
        
        return dfs(0,0)