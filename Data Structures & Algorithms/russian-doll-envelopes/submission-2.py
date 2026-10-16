class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # find a strictly increasing path?
        # longest strictly increasing path
        # at each step compute the longest strictly increasing
        # path from this envelope
        
        # why can this not be greedy?
        # is it faster to do this with dp?
        # greedy is o(nlogn) dp is o(n)

        # try it with dp
        
        # initially sort by width and then sort by height
        # then we don't need to loop through everything
        # we just need to loop from j to n
        # and we don't need visited

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        memo = {}
        def dfs(i):
            # look at the values we can explore from here
            if i in memo:
                return memo[i]
            curr = envelopes[i]
            currlen = 0
            for j in range(i+1, len(envelopes)):
                comp = envelopes[j]
                comp_tuple = tuple(comp)
                if comp[0] > curr[0] and comp[1] > curr[1]:
                    currlen = max(currlen, 1+dfs(j))
            memo[i] = currlen
            return currlen

        maxlen = 0
        for i in range(len(envelopes)):
            maxlen = max(maxlen, 1 + dfs(i))
        
        return maxlen
            
