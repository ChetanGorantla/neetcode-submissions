class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place for each row in the curr col
        # go col by col until col out of bounds
        out = []
        grid = [["."] * n for i in range(n)]

        def tryQueen(r):
            if r == n:
                returnArr = ["".join(row) for row in grid]
                out.append(returnArr)
                return
            
            for c in range(n):
                # try to place in this row
                if (self.isSafe(r,c,grid)):
                    grid[r][c] = 'Q'
                    tryQueen(r+1)
                    grid[r][c] = '.'

        tryQueen(0)
        return out
    

    def isSafe(self, r: int, c: int, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True
                