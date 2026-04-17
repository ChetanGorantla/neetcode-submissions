class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # so we're basically just filling visited squares and 
        # counting how many times we enter an unvisited land
        # when we call our dfs method in a double for loop
        count = 0
        visited = [[False for i in range(len(grid[0]))] for row in range(len(grid))]

        def dfs(r,c):
            
            # if r,c out of bounds or we're on water, exit
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == "0"):
                return
            # if r,c already visited, exit
            if (visited[r][c]):
                return
            # if we're on land, continue exploring all paths
            # mark as visited
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return
        

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    count+=1
                    dfs(i,j)
        return count