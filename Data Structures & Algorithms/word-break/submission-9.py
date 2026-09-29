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
        # now let's do it bottom-up
        # we need to maintain a dp array of length s+1
        # last element needs to be True
        dp = [False] * (len(s)+1)
        # this signals that we can reach the end from the last index
        dp[len(s)] = True

        # at each index in dp, we need to traverse forwards to any extent
        # with any word in wordDict
        # if so, this value equals that value
        for i in range(len(dp)-2, -1, -1):
            # we're at an index. look at all words we can explore
            for word in wordDict:
                # if this reaches past where our dp array ends, continue
                if i + len(word) >= len(dp) or s[i:i+len(word)] != word:
                    continue
                
                # this doesn't reach past the end.
                # we can safely explore this.
                # just survey if it's possible, so break upon
                # first success.
                if dp[i+len(word)]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]

