class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = []
        #visited should store i,j pairs (coords)
        def explore(r,c):
            #if this is out of bounds or this is water, then we have found an edge
            # return 1
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0):
                return 1
            if ([r,c] in visited):
                return 0
            #if this is in bounds and equals land, then explore all directions to locate
            #non-land
            #explore the directions
            visited.append([r,c])
            perimeter = explore(r+1, c) + explore(r-1, c) + explore(r, c+1) + explore(r, c-1)
            return perimeter

        
        #explore all grid values
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]):
                    return explore(i,j)
        return 0
