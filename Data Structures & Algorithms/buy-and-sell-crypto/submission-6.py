class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit possible
        # maintain a minimum buy
        buy = sys.maxsize
        sell = 0
        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price-buy)
        return sell