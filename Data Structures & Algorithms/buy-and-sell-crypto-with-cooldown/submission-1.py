class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # instead of storing cooldown state, just skip
        # only process days you can buy
        # on those days, either buy or skip
        
        # at each step, we're at an index where we could make a decision.
        # let's make the decision to either skip today, or buy and sell for
        # a future date.
        # that means we need to track our current index

        memo = {}
        def dfs(i):
            if i >= len(prices):
                return 0
            
            if i in memo:
                return memo[i]
            
            total = 0
            # don't buy
            total = max(total, dfs(i+1))
            # try to explore all options
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    total = max(total, prices[j]-prices[i] + dfs(j+2))
            memo[i] = total
            return total
        
        return dfs(0)
            