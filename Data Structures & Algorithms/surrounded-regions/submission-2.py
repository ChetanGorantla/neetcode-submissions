class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # when you find land, backtrack to find all spaces
        # it is connected to. If any of these are on the border,
        # this entire surface is invalid. We don't want to edit any
        # groups that are connected to the border.
        
        # so when we recurse, first check if we have visited this spot
        # if we haven't, continue

        # then, if this spot is O, continue
        # then, if this spot is on the border, return false

        # basically we need to check first if this subgrid is valid
        # store the validity in a variable.
        # if validity is true, then we can color this
        # if validity is false, we cannot color this.
        # return validity to pass it up the stack frame

        visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]

        def dfs(r, c):
            
            if ((r >= 0 and r < len(board) and c >= 0 and c < len(board[r])) and board[r][c] == "O"):
                # visit this spot
                # mark the complementary graphs that we cannot count
                board[r][c] = "#"
                dfs(r+1,c)
                dfs(r-1, c)
                dfs(r, c-1)
                dfs(r, c+1)
        
        for j in range(len(board[0])):
            dfs(0,j)
            dfs(len(board)-1, j)
        
        for i in range(len(board)):
            dfs(i,0)
            dfs(i, len(board[i])-1)
        
        # capture
        for i in range(len(board)):
            for j in range(len(board[i])):
                # don't change 
                if (board[i][j] == "O"):
                    board[i][j] = "X"
                elif (board[i][j] == "#"):
                    board[i][j] = "O"
        
        
        
        
        
