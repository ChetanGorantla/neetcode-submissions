class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # at each step, for all the coins within the coin-space that are within the amount
        # recursively call on the subtracted value
        # memoize based on the current amount to fill, and the current coin to select
        
        # at each step, choose whether or not to use the current coin
        # if we use this coin reduce the total amount
        # either way, based on the total amount (updated if possible), explore all possible combinations
        # of coins that are less than the total amount

        # memoize based on the total amount and the index of the next coin to choose from
        
        memo = {}
        # (i, amt) : ways

        def search(i, amt):
            if i == len(coins):
                return 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            if amt < 0:
                return 0
            
            if amt == 0:
                return 1

            # we have not explored this yet
            # choose to use the coin
            use = search(i, amt-coins[i])
            skip = search(i+1, amt)

            ways = use + skip

            memo[(i, amt)] = ways
            return ways
        
        #print(memo)
        return search(0, amount)
