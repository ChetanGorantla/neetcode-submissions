class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs

        #visited = [([False] * len(grid[0]))for __ in range(len(grid))] 

        def dfs(r, c):
            #print(r,c)
            # out of bounds case
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])):
                return 0
            if grid[r][c] == 0 or grid[r][c] == -1:
                return 0
            # not explored this yet
            #if visited[r][c]:
            #    return 0
            
            # explore all edges
            
            grid[r][c] = -1
            total = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)
            #grid[r][c] = 1
            return total

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_area = max(max_area, dfs(i,j))
        
        return max_area

