class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at each step we need to choose whether we want to sell on this date or hold
        # memoize the maximum profit you can achieve from this coin to the end of the prices
        # memoize based on whether or not we can buy on this day
        # (i, t/f) : profit
        memo = {}

        def explore(i, canBuy):
            if i >= len(prices):
                return 0
            
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            
            
            
            # we have not explored this yet.
            # we need to choose whether or not to buy this

            if canBuy:
                # if we can buy at this step, we have a choice to either buy, or not buy
                # figure out the maximum of the two
                buy = explore(i+1, False) - prices[i]
                skip = explore(i+1, True)
                profit = max(buy, skip)
            else:
                # if we cannot buy at this step, we have a choice to either sell, or hold
                sell = prices[i] + explore(i+2, True)
                hold = explore(i+1, False)
                profit = max(sell, hold)
                
            
            # store profit
            memo[(i, canBuy)] = profit
            return profit
        
        explore(0, True)
        print(memo)
        return memo[(0, True)]
                