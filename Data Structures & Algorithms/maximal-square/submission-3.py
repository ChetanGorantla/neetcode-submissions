class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # maintain a tracker array to see the length this square can extend to
        # initialize to -1 which marks unvisited
        # upon computation, mark as the actual count
        # if curr is 1
        # explore 3 directions: right, down, diag, and the current area is 1 + min(right, down, diag)
        
        # if curr is 0, return 0
        areas = {}
        
        # initialized the memo table, start dfs

        def dfs(r, c):
            # if out of bounds, exit
            if r >= len(matrix) or c >= len(matrix[0]):
                return 0
            # if already computed, return the value
            if (r, c) in areas:
                return areas[(r,c)]
            
            # if this isn't a 1, return 0
            

            # this is a 1
            # we need to compute the possibilities
            # set curr to the minimum + 1
            # either way if this is a 1 or 0, it'll still compute the areas, so we don't need to do a mxn
            # loop outside to call dfs each time
            area = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
            areas[(r,c)] = 0
            if matrix[r][c] == "1":
                areas[(r,c)] = area
            return areas[(r,c)]
        
        dfs(0,0)
        return max(areas.values()) ** 2