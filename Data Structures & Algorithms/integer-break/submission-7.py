class Solution:
    def integerBreak(self, n: int) -> int:
        # maximize the product 
        # so we can maybe do dp such that we are splitting a number n into 2 different numbers
        # and we split those and so on and so forth
        # where we want to maximize the overall product of these two (dp left x dp right)

        # but again, we want to be summing two integers
        # the maximum product occurs when numbers are close together
        # so maybe start inside out?
        # say we have n
        # we want to split this first into n/2 + n/2 and split those as such
        # if this integer cannot be split evenly (it's odd) then we need to get the upper and lower
        # (21/2 = 10.5 so that's 10 + 11 (floor + ceil))


        # the dp is memoization based on n
        # compute the maximum possible product we can have at a given n
        if n == 2:
            return 1

        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]

            # base case is if it's one or two, we can't split it down further
            if n == 1:
                return 1

            # haven't computed this integer yet

            # split everywhere we can instead of only doing a middle split
            # split from 1 to n
            res = 0
            # repeats after halfway (ceil(n/2)), can optimize here
            for i in range(1, math.ceil(n/2)+1):
                res = max(res, n, dfs(i) * dfs(n-i))
            res = int(res)
            print(n, res)
            memo[n] = res
            return res

        # we can solve the issue of not having at least 2 distinct values by forcing that first
        res = 0
        for i in range(1, math.ceil(n/2)+1):
            res = max(res, dfs(i) * dfs(n-i))
        res = int(res)
        print(n, res)
        memo[n] = res
        return res
