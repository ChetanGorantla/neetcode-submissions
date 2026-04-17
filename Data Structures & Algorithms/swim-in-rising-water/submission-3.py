class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we need to perform dfs and at each step, either pursue a route or stay here
        # increment time in the function call
        
        # explore all paths to reach the end
        # track the largest value in the path
        # once we've reached the end update the max value along the path

        # scratch the dfs and 2d dp

        # this is a dijkstra problem

        # start from the end node
        # trace backwards to the origin

        # maintain a priority queue of the distance between this node and the ending node
        # minheap
        # lower distances go first
        # because if we poll lower distances and reach the origin then we've done it optimally

        # store values in the heap as (distance, r, c)
        target = grid[len(grid)-1][len(grid[0])-1]

        minheap = []

        heapq.heappush(minheap, (0, len(grid)-1, len(grid[0])-1))
        maxheight = 0

        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]

        def inBounds(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

        while minheap:

            # poll
            curr = heapq.heappop(minheap)
            print("Visiting " + str(curr))
            distance = curr[0]
            r = curr[1]
            c = curr[2]

            if r == 0 and c == 0:
                return max(maxheight, grid[r][c])
            
            if not visited[r][c]:
                visited[r][c] = True
                maxheight = max(maxheight, grid[r][c])

                # explore all choices
                if inBounds(r+1, c):
                    heapq.heappush(minheap, (grid[r+1][c] - target, r+1, c))
                if inBounds(r-1, c):
                    heapq.heappush(minheap, (grid[r-1][c] - target, r-1, c))
                if inBounds(r, c+1):
                    heapq.heappush(minheap, (grid[r][c+1] - target, r, c+1))
                if inBounds(r, c-1):
                    heapq.heappush(minheap, (grid[r][c-1] - target, r, c-1))
        
        return maxheight
                

        

