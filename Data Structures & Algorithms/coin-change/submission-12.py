class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # maintain a dp array
        # we need to say, at a current amount, how many ways
        # can we get to here from all previous denoms?
        # pic 1 + the minimum and set
        
        # min coins needed for previous denoms
        dp = [0]*(amount+1)

        

        for i in range(1, len(dp)):
            # look at all possible coin combos that have >= amt
            needed = sys.maxsize
            for amt in coins:
                if i - amt >= 0:
                    needed = min(needed, dp[i-amt])
            
            dp[i] = 1 + needed
        
        return -1 if dp[amount] > amount else dp[amount]
