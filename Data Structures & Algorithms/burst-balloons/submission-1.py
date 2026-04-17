class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # we need to simulate bursting the balloons
        # memoize based on the left value to multiply and the right value to multiply and the overall
        # sum of the continuation from there?
        memo = {}

        # for each value in the current problem, what if we pop it last?
        # and then break down into 2 subarrays
        # keep implicit bounds for coin values

        # store (l, r) in memo and store the total coins you can achieve from this subarray
        # loop thru each value in l and r and try to pop these last
        # and store the max out of all those attempts
        coins = [1] + nums + [1]

        def explore(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            
            # we have not explored this subarray yet.
            # loop thru it, and at each step, choose whether or not to pop this value last
            maxcoins = 0
            for i in range(l, r+1):
                totalcoins = coins[l-1] * coins[i] * coins[r+1]
                totalcoins += explore(l, i-1) + explore(i+1, r)
                maxcoins = max(maxcoins, totalcoins)
            
            memo[(l,r)] = maxcoins
            return maxcoins
        
        return explore(1, len(coins)-2)
            

