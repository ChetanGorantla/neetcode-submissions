class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rottens
        # only accept fresh fruits
        # maintain level
        # return overall level

        level = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        # perform bfs
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        processed = False
        while queue:
            qlen = len(queue)
            processed = True
            taken = False
            for i in range(qlen):
                curr = queue.popleft()
                # ensure this is fresh
                r, c = curr[0], curr[1]
                if grid[r][c] != 1 and level > 0:
                    continue

                taken = True
                # mark this cell as rotten
                grid[r][c] = 2
                for [xdir, ydir] in directions:
                    newr, newc = r + xdir, c + ydir
                    
                    # if our extension is not: in bounds and fresh, continue
                    if not ((newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[newr])) and grid[newr][newc] == 1):
                        continue
                    
                    # this is in bounds and fresh
                    
                    queue.append([newr, newc])
            if taken:
                level+=1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        # only return level-1 if we entered the queue system
        # otherwise return 0
        return level-1 if processed else 0
        
        # look to see if there's any fresh