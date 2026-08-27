class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # curr should be the sum of up and left
        # 1, 1 should be 1
        dfs = [[0 for _ in range(len(obstacleGrid[0])+1)] for __ in range(len(obstacleGrid)+1)]

        # loop through 1, len(dfs)
        # obstacleGrid must be accessed at ind-1
        # if obstacleGrid == 1, skip this
        
        dfs[0][1] = 1
        for i in range(1, len(dfs)):
            for j in range(1, len(dfs[i])):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                
                dfs[i][j] = dfs[i-1][j] + dfs[i][j-1]
        print(dfs)
        return dfs[-1][-1]