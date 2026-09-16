class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # after we explore a valid cell, we need to mark it as 0
        # and add 1 + dfs(explorations)
        # and return that

        def dfs(r, c):
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])):
                return 0
            
            # in bounds
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            total = 0
            if grid[r][c] == 1:
                grid[r][c] = 0
                # explore all directions
                total = 1
                for [xdir, ydir] in directions:
                    total += dfs(r + xdir, c + ydir)

            return total

        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = dfs(i,j)
                maxarea = max(maxarea, area)
        return maxarea