class Solution:
    def numDecodings(self, s: str) -> int:
        # we're just counting the number of ways
        # at each step, count ways to either process one number or two numbers

        # maybe we pass through a variable that determines if our
        # path is valid
        # but that can be implicit
        # memoize
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            # we're not at the end yet
            # we can always do one
            total = 0
            if s[i] != "0":
                total += dfs(i+1)
                if i < len(s)-1 and 1 <= int(s[i:i+2]) <= 26:
                    total += dfs(i+2)
            memo[i] = total
            return total

        
        return dfs(0)