class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we need to store memoized results inside of a 2d array
        # that stores the moves from origin to the current grid
        # at each step, to compute the number of moves, take the uniquePaths result of left
        # and the uniquePaths result of top and add them together
        # that makes curr
        # at each step, we can either explore down or right

        memo = [[0 for _ in range(n)] for __ in range(m)]

        memo[0][0] = 1
        def explore(r,c):
            if r < 0 or c < 0:
                return 0
            
            if memo[r][c] != 0:
                return memo[r][c]
            
            # we have not explored this cell yet
            # compute the score
            memo[r][c] = explore(r-1, c) + explore(r, c-1)
        
        for i in range(m):
            for j in range(n):
                explore(i,j)
        #print(memo)
        return memo[-1][-1]