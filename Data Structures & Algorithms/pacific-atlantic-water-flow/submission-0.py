class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        pacific = set()
        atlantic = set()
        
        def dfs(r, c, prev, this):
            
            if (r >= 0 and r < len(heights) and c >= 0 and c < len(heights[r])) and (r, c) not in this and (heights[r][c] >= prev):
                this.add((r,c))
                
                dfs(r+1, c, heights[r][c], this)
                
                dfs(r-1, c, heights[r][c], this)
                
                dfs(r, c+1, heights[r][c], this)
                
                dfs(r, c-1, heights[r][c], this)

                

        # add all pacifics and atlantics
        for i in range(len(heights)):
            dfs(i, 0, heights[i][0], pacific)
        for i in range(len(heights[0])):
            dfs(0, i, heights[0][i], pacific)

        

        for i in range(len(heights)):
            dfs(i, len(heights[0])-1, heights[i][len(heights[0])-1], atlantic)
        for i in range(len(heights[0])):
            dfs(len(heights)-1, i, heights[len(heights)-1][i], atlantic)
        print(pacific)
        print(atlantic)
        out = []
        # check duplicates
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if ((r, c) in atlantic and (r, c) in pacific):
                    out.append([r,c])
        return out


                

        
