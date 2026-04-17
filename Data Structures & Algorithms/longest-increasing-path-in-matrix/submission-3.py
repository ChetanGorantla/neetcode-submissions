class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # store memoized results based on coordinates
        # store the length of the increasing path starting from this value at this coordinate
        inf = sys.maxsize
        memo = {}

        # we want to be able to backtrack across our matrix
        # at each step, look to see if we're out of bounds, exit
        # if we're already in memo, return the value

        # if prev <= curr, return 0 because this route is invalid
        
        # otherwise we haven't explored it and this is an increasing path to explore
        # only explore options that are greater than the current value
        # so when we go thru the directions
        # and take max(up down left right)
        
        # and set memoized result to this extension

        def search(prev, r, c):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
                return 0

            curr = matrix[r][c]
            if prev <= curr:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            
            
            # we have not explored this path, but it is a valid extension.
            # we want to extend this path
            
            path = 1 + max(search(curr, r+1, c), max(search(curr, r-1, c), max(search(curr, r, c+1), search(curr, r, c-1))))
            memo[(r,c)] = path
            return path
        
        # for all values compute the max

        globalmax = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                globalmax = max(globalmax, search(inf, i, j))
        
        return globalmax
