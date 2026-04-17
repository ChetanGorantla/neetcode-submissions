class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        
        def dfs(r,c):
            # if out of bounds or visited, break
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or [r,c] in visited):
                return 0
            if (grid[r][c] == 0):
                return 0
            visited.append([r,c])
            area = grid[r][c]
            #sum up top down left and right
            #return sum
            area += dfs(r,c+1) + dfs(r,c-1) + dfs(r+1, c) + dfs(r-1, c)
            return area
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if ([i,j] not in visited):
                    area = dfs(i,j)
                    print(area)
                    maxarea = max(maxarea, area)
        return maxarea