class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # given a balance of x, smallest # of ways can you get to 0?
        # at a given balance, you backtrack across all possible paths
        memo = {}
        inf = sys.maxsize

        def explore(curr):
            if curr == 0:
                return 0
            if curr in memo:
                return memo[curr]
            
            # we have not computed the value for this.
            # we need to explore
            val = inf
            for coin in coins:
                if coin <= curr:
                    # explore this path
                    #print("Exploring " + str(curr-coin))
                    currcount = 1 + explore(curr-coin)
                    val = min(currcount, val)
            memo[curr] = val
            return val
        
        
        mincoins = explore(amount)
        #print(counts)
        if mincoins == inf:
            return -1
        return mincoins

            