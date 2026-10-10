class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # can only swim equivalent or down
        # min time to go from bottom left to bottom right
        # at each step we need to consider the smallest grid value 
        # that we can explore out of all adjacents
        # store the max value from start to this point
        # store a hashmap of max val from path
        # at each cell, store the max value from start to this point
        # that way when we try to explore an edge, we can say cost
        # to get to dest = max(maxpath[source], grid[dest])
        
        # maxpath also serves as our visited tracker
        # don't try to re-explore a cell already in maxpath

        maxpath = {(0,0):0}
        # heap stores (grid cost, r, c)
        heap = [(grid[0][0], (0, 0), (0,0))]
        
        while True:
            # take candidate
            curr = heapq.heappop(heap)
            #print(curr)
            currcost = curr[0]
            source = curr[1]
            dest = curr[2]
            # update maxpath
            maxpath[dest] = max(currcost, maxpath[source])
            # if we're at the end, return this value
            r = dest[0]
            c = dest[1]
            if r == len(grid)-1 and c == len(grid[r])-1:
                return maxpath[dest]

            # explore neighbors
            for dirx, diry in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                newr = r+dirx
                newc = c+diry
                if (newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[newr]) and (newr, newc) not in maxpath):
                    # in bounds and not explored. add to heap
                    heapq.heappush(heap, (grid[newr][newc], dest, (newr, newc)))
        return -1