class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bottom-up 2d dp array
        # at a cell, we want to compute the minimum path to here
        # the only option is to compare which is smaller: up or left
        # and choose that to update curr (+=)

        dfs = [[0 for _ in range(len(grid[0])+1)] for __ in range(len(grid)+1)]

        # the two starting ones must be 0
        # all other edge ones must be sys.maxsize
        for i in range(2, len(dfs)):
            dfs[i][0] = sys.maxsize
            
        for j in range(2, len(dfs[0])):
            dfs[0][j] = sys.maxsize


        for i in range(1, len(dfs)):
            for j in range(1, len(dfs[i])):
                # grid value + the min connector
                dfs[i][j] = grid[i-1][j-1] + min(dfs[i-1][j], dfs[i][j-1])
        print(dfs)
        return dfs[-1][-1]