class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # capture surrounded regions
        # we need to check to see if this reaches the border
        # if it does, then we replace with an X

        # at each step we need to check to see if it reaches X

        # use iterative bfs
        # only go based on each connected component at a time
        # maintain our overall list
        # and if we exit out of our queue without ever reaching a border,
        # we can go back and replace all of these
        # maintain a set of visited so we don't reexplore within our overall
        
        # we should return T/F (reached border) and update a value
        # in the parameters (cells) that we need to update in our overall loop
        # based on the result of the function call
        visited = set()
        def bfs(r, c, traversed):
            queue = deque()
            queue.append((r, c))
            result = False
            while queue:
                qlen = len(queue)
                for k in range(qlen):
                    i, j = queue.popleft()
                    if (i,j) in visited:
                        continue
                    # we need to check to see if this is outside of scope
                    # if it is, that means we had a border
                    if not (i in range(len(board)) and j in range(len(board[i]))):
                        result = True
                        continue
                    
                    # this is in range
                    # explore neighbors only if this is an O
                    if board[i][j] == "X":
                        continue

                    # this is an inbounds, connected component O
                    visited.add((i,j))
                    traversed.append((i,j))
                    # this is an O
                    # explore neighbors
                    queue.append((i+1, j))
                    queue.append((i-1, j))
                    queue.append((i, j+1))
                    queue.append((i, j-1))
            return result
        
        # loop through our entire search space while not visited
        for i in range(len(board)):
            for j in range(len(board[i])):
                traversed = []
                replace = False
                if (i,j) not in visited and board[i][j] == "O":
                    
                    replace = not bfs(i,j,traversed)
                
                if replace:
                    for x, y in traversed:
                        board[x][y] = "X"
        
                
