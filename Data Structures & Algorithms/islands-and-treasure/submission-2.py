class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # fill in with distance to nearest treasure chest
        # bfs from treasure chests
        # if a square is not inf then continue, this has already
        # been explored or its not explorable
        # initially populate our queue with the treasure chests
        # if the neighboring cell is out of bounds or doesn't equal inf then
        # continue
        inf = 2147483647
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        # queue is populated with [i,j]
        # perform bfs
        # at each step, set to level
        level = 0
        directions = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                [r, c] = queue.popleft()
                if grid[r][c] != 0 and grid[r][c] != inf:
                    continue
                #print(f"Exploring {r}, {c}")
                grid[r][c] = level
                # explore neighbors that are valid explorations
                for [xdir, ydir] in directions:
                    newr = r+xdir
                    newc = c+ydir
                    if not (newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[newr])) or grid[newr][newc] != inf:
                        continue
                    
                    # this is a valid extension to add to our queue
                    queue.append([newr, newc])
            level+=1
        
        

