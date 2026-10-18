class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # count the diff sequences of moves that take the ball outside the grid w 
        # at most maxMove moves

        # we cannot repeat paths because of the nature of our backtracking approach
        # so we don't need to store the path itself or visited
        # we can just make a move at a certain cell
        # if we are outside of the grid then return 1
        # if we have no moves left return 0

        # we can memoize?
        MOD = 1000000007
        memo = {}
        def explore(r, c, movesLeft):
            if (r, c, movesLeft) in memo:
                return memo[(r, c, movesLeft)]
            if not (r >= 0 and r < m and c >= 0 and c < n):
                return 1
            
            if movesLeft == 0:
                return 0
            
            # we are still in the grid and have moves left
            # make a decision
            sequences = 0
            for dirx, diry in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                sequences+=explore(r+dirx, c+diry, movesLeft-1)
                sequences %= MOD
            
            memo[(r, c, movesLeft)] = sequences
            return sequences
        
        return explore(startRow, startColumn, maxMove)
