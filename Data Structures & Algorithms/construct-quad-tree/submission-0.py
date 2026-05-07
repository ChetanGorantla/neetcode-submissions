"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    
        def dfs(r, c, s):
            # construct a node based on the inputs and return it

            # base case, singular block
            if s == 1:
                return Node(grid[r][c], 1, None, None, None, None)
            
            # loop over the entire space
            
            leaf = True
            for i in range(s):
                for j in range(s):
                    if grid[r+i][c+j] != grid[r][c]:
                        # not a leaf
                        leaf = False


            # is a leaf
            if leaf:
                return Node(grid[r][c], 1, None, None, None, None)

            # not a leaf
            s = int(s/2)
            tl = dfs(r, c, s)
            tr = dfs(r, c+s, s)
            bl = dfs(r+s, c, s)
            br = dfs(r+s, c+s, s)
            return Node(-1, False, tl, tr, bl, br)
        
        return dfs(0, 0, len(grid))
