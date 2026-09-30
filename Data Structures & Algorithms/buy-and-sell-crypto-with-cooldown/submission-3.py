class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # instead of storing cooldown state, just skip
        # only process days you can buy
        # on those days, either buy or skip
        
        # at each step, we're at an index where we could make a decision.
        # let's make the decision to either skip today, or buy and sell for
        # a future date.
        # that means we need to track our current index

        # modify so we're doing 2d dp
        # at each step, we need to store the index we're on and whether
        # we're holding something at this point
        # always attempt to continue the state to the next index
        # if we're holding, then try to sell
        # if we're not holding, then try to buy

        memo = {}
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            # we are not at the end yet
            total = 0
            # we can always try to skip
            total = max(total, dfs(i+1, holding))
            if holding:
                # let's try to sell
                total = max(total, prices[i] + dfs(i+2, False))
            else:
                # let's try to buy
                total = max(total, -prices[i] + dfs(i+1, True))
            
            memo[(i, holding)] = total
            return total
        return dfs(0, False)