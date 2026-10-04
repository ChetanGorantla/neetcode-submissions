class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check to see the index in the word we're looking for
        # if the index is the length, we're done looking
        # that should be our first check

        def explore(i, r, c):
            if i == len(word):
                return True
            
            # we're not done searching
            # ensure we're in bounds
            if not (r >= 0 and r < len(board) and c >= 0 and c < len(board[r])):
                return False
            
            # we're in bounds but not at the end of our search.
            # check to see if this character matches
            if word[i] != board[r][c]:
                return False
            
            # this character matches. let's explore all possible ways
            possible = False
            # ensure we don't revisit the current value
            board[r][c] = "*"
            for xdir, ydir in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                
                possible = possible or explore(i+1, r+xdir, c+ydir)

            board[r][c] = word[i]
            return possible
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if explore(0, i, j):
                    return True
        
        return False