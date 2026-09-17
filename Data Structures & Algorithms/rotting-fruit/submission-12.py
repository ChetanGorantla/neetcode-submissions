class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rottens
        # only accept fresh fruits
        # maintain level
        # return overall level

        level = 0
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh+=1
        
        # perform bfs
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while queue and fresh > 0:
            qlen = len(queue)
            for i in range(qlen):
                r, c = queue.popleft()

                # look at new directions
                for xdir, ydir in directions:
                    newr, newc = r + xdir, c + ydir
                    # process when adding the new bananas
                    if newr in range(len(grid)) and newc in range(len(grid[newr])) and grid[newr][newc] == 1:
                        fresh-=1
                        grid[newr][newc] = 2
                        queue.append([newr, newc])
            level+=1
        return level if fresh == 0 else -1
        # look to see if there's any fresh