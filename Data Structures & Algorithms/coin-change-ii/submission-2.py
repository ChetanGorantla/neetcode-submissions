class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # distinct combinations that add up to amount
        # at each value, we can add any amount as long as it doesn't exceed target
        # let's do this top-down first
        # at each stage, we can either add this coin value or skip this coin value

        # we need to track the current target and the index in coins we're at
        

        # at each coin value and target value, we need to see how many ways we've gotten here
        # that's computed by seeing if we either previously took this same coin value and
        # stayed at the coin value, or skipped the previous coin value and went straight
        # to this value from the same amount
        # so sum up [amount-coin][coin] and [amount][coin-1]


        dp = [[0 for _ in range(len(coins)+1)] for __ in range(amount+1)]

        # there is a way to get an amount of 0 at every coin, to not take it.
        
        for j in range(1, len(coins)+1):
            dp[0][j] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                # i represents amount, j represents ind in coins
                # say we have amount 1 and are at coin value 1

                # if the amount we're taking doesn't dip below 0, count it
                if i-coins[j-1] >= 0:
                    dp[i][j] = dp[i-coins[j-1]][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
                # otherwise, we must have skipped
        #print(dp)
        return dp[amount][len(coins)]
