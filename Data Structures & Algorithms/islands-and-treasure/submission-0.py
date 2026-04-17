class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        inf = 2147483647
        # if not currently on a square we visited
        # if currently on a treasure chest, return 0
        # if currently on a water cell that cannot be traversed, return inf
        # if currently on a land cell,
        # int traversal = min(dfs(up), dfs(down), dfs(left), dfs(right))
        # grid[r][c] = traversal
        # return traversal 

        
        # start from all chests
        # if the current cell is a chest, do dfs on all directions
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 0):
                    queue.append([i,j])
        # search for all chests and add into the queue
        # while the queue is not empty
        # dequeue a cell
        # set it's grid value to the current level
        # enqueue all of it's neighbors that have not been visited and are land
        level = 0
        
        while queue:
            # get all the cells in the initial queue
            qsize = len(queue)
            print(level)
            for i in range(qsize):
                cell = queue.popleft()
                print(cell, level)
                r = cell[0]
                c = cell[1]
                
                grid[r][c] = level
                # enqueue valid neighbors
                if (r-1 >= 0 and not visited[r-1][c] and grid[r-1][c] == inf):
                    queue.append([r-1, c])
                    visited[r-1][c] = True
                if (r+1 < len(grid) and not visited[r+1][c] and grid[r+1][c] == inf):
                    queue.append([r+1, c])
                    visited[r+1][c] = True
                if (c-1 >= 0 and not visited[r][c-1] and grid[r][c-1] == inf):
                    queue.append([r, c-1])
                    visited[r][c-1] = True
                if (c+1 < len(grid[r]) and not visited[r][c+1] and grid[r][c+1] == inf):
                    queue.append([r, c+1])
                    visited[r][c+1] = True
            level+=1


