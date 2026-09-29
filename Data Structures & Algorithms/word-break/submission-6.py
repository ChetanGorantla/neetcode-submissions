class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we need to take on whole words at once rather than going
        # index by index
        # at a certain index, see which words we can use
        # explore those options
        # backtrack as necessary
        # within our exploration loop we need to ensure that we stay in bounds
        # with this word


        # at a certain point, store if it's possible to reach the end from here
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
                
            # we're not at the end yet.
            # explore all options we have
            possible = False
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    # explore this, its valid
                    possible = possible or dfs(i+len(word))
            memo[i] = possible
            return possible
        
        return dfs(0)