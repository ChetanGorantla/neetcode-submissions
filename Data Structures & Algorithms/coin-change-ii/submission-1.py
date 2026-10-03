class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # distinct combinations that add up to amount
        # at each value, we can add any amount as long as it doesn't exceed target
        # let's do this top-down first
        # at each stage, we can either add this coin value or skip this coin value

        # we need to track the current target and the index in coins we're at
        memo = {}

        def dfs(i, target):
            
            if target == 0:
                return 1
            if target < 0:
                return 0
            # we are not at target yet
            # we need to see if we have any more coins to choose from
            if i == len(coins):
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            # either take or don't take
            ways = dfs(i+1, target) + dfs(i, target-coins[i])
            memo[(i, target)] = ways
            return ways
        
        return dfs(0, amount)