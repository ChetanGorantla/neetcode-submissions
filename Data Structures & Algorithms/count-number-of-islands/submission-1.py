class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we need to count every time we encounter a 1 in our overall
        # search space.
        # when we encounter a 1, we need to replace it with 0 and explore
        # all neighbors
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c):
            # check to see if it's out of bounds
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])):
                return

            # in bounds and a land mass
            if grid[r][c] == "1":
                grid[r][c] = "0"
                for [xdir, ydir] in directions:
                    dfs(r+xdir, c+ydir)
            
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    c+=1
                    dfs(i, j)

        return c
                