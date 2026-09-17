class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # create a set of all values in pacific and atlantic paths
        # we need to explore cells that are of heigh >= curr
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited):
            # at a given stage, only explore options that extend

            for xdir, ydir in directions:
                newr, newc = r + xdir, c + ydir
                # add to set and explore if valid
                if (newr in range(len(heights)) and newc in range(len(heights[newr])) and (newr, newc) not in visited and heights[newr][newc] >= heights[r][c]):
                    visited.add((newr, newc))
                    dfs(newr, newc, visited)
        
        # populate pacific and atlantic
        atlantic = set()
        pacific = set()
        for i in range(len(heights)):
            if (i, 0) not in pacific:
                pacific.add((i,0))
                dfs(i, 0, pacific)
            if (i, len(heights[i])-1) not in atlantic:
                atlantic.add((i, len(heights[i])-1))
                dfs(i, len(heights[i])-1, atlantic)
        for j in range(len(heights[0])-1):
            if (0, j+1) not in pacific:
                pacific.add((0, j+1))
                dfs(0, j+1, pacific)
            if (len(heights)-1, j) not in atlantic:
                atlantic.add((len(heights)-1, j))
                dfs(len(heights)-1, j, atlantic)
        
        # return the mutuals
        #print(pacific)
        #print(atlantic)
        out = []
        pacific_list = list(pacific)
        for coord in pacific_list:
            if coord in atlantic:
                out.append([coord[0], coord[1]])
        return out