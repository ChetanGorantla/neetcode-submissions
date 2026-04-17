class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # go level by level outwards in 
        # at each value in each level, make 4 swap trips for the corresponding
        # axes
        n = len(matrix)
        levels = n-1
        level = 0

        while level < levels:
            # initial row is at the current level
            # from cols level -> n-level
            row = matrix[level]

            for i in range(level, n-level-1):
                # make 4 swap trips
                
                swaps = [(level, i), (n-i-1, level), (n-level-1, n-i-1), (i, n-level-1)]
                print(swaps)
                for j in range(1, len(swaps)):
                    prev = swaps[j-1]
                    curr = swaps[j]
                    temp = matrix[prev[0]][prev[1]]
                    matrix[prev[0]][prev[1]] = matrix[curr[0]][curr[1]]
                    matrix[curr[0]][curr[1]] = temp
            level+=1
        #return matrix


                    
