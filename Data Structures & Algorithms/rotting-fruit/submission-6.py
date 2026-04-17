class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # perform bfs and count the max number of levels traversed when an unvisited
        # rotten fruit is found

        # at the end, loop thru the whole matrix to see if there are any fresh fruits left
        # if there are, return -1.
        # if there aren't, return the max levels computed
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        minlevel = sys.maxsize
        queue = deque()
        def bfs():
            
            level = 0
            # pop a value
            while queue:
                nonlocal minlevel
                qsize = len(queue)
                print(level)
                foundBanana = False
                # loop thru the current queue
                for i in range(qsize):
                    coords = queue.popleft()
                    r = coords[0]
                    c = coords[1]
                    # check if not visited yet and in bounds
                    if (r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r]) and not visited[r][c]):
                        
                        # if rotten, continue exploring
                        # if not rotten, mark as rotten and continue exploring
                        if grid[r][c] == 0:
                            continue
                        print(f"Exploring cell {r}, {c} with value {grid[r][c]}")
                        visited[r][c] = True
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                        foundBanana = True
                        # explore neighbors
                        queue.append([r+1, c])
                        queue.append([r-1, c])
                        queue.append([r, c+1])
                        queue.append([r, c-1])
                if (foundBanana):
                    level+=1
            level-=1
            minlevel = min(level, minlevel)
            
        def spreadable(r,c):
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i >= 0 and j >= 0 and i < len(grid) and j < len(grid[r])):
                        if (not (i == r and j == c)):
                            if (grid[i][j] == 1):
                                return True
            return False

            
        # only enqueue rotten bananas that have a good banana around it
        numgoods = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    numgoods+=1
                if not visited[i][j] and grid[i][j] == 2 and spreadable(i,j):
                    queue.append([i,j])
        
        # exit early if there are no rotten bananas 
            # if there are no good bananas return 0
            # if there are good bananas return -1
        if not queue:
            if numgoods == 0:
                return 0
            else:
                return -1
        bfs()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    return -1
        if (minlevel == sys.maxsize):
            return 0
        return minlevel
    

