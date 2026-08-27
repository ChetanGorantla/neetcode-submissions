class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we need to explore all of the coins we can use based on amount
        # only use

        # store the current amount and the index we're trying to add a coin for
        memo = {}
        def dfs(needed):
            if needed == 0:
                return 0
            if needed in memo:
                return memo[needed]
            # we need more
            total = 1e9
            for j in range(len(coins)):
                # early exit condition
                if needed-coins[j] >= 0:
                    
                    total = min(total, 1 + dfs(needed-coins[j]))
            memo[needed] = total
            return total
        
        ans = dfs(amount)
        print(ans)
        if ans == 1e9:
            return -1
        return ans
