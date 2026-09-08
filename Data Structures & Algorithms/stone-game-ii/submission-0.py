class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # return the maximum number of stones alice can get
        # we want to perform dp based on the index within the pile and the m value
        # at a certain m, we need to loop through 1 to 2M and try all of those options

        # should we maintain a prefix sum array so we can quickly compute the score
        # between i + j and i?
        sums = [0] * (len(piles)+1)
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + piles[i-1]
        
        #print(sums)
        memo = {}
        def explore(i, m):
            # reached the end of the list
            if i >= len(piles):
                return 0
            
            if (i,m) in memo:
                return memo[(i,m)]
            
            # we haven't explored this yet. choose optimally from this player's perspective
            decision = -sys.maxsize
            for j in range(i, i + 2*m):
                # try to explore this
                # compute prefix sum from i to j inclusive
                if j+1 >= len(sums):
                    break
                #print(i, j, sums[j+1]-sums[i])
                decision = max(decision, sums[j+1]-sums[i] - explore(j+1, max(j-i+1, m)))
            
            memo[(i,m)] = decision
            return decision
        
        return (sum(piles) + explore(0, 1))//2
            
