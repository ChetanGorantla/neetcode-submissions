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
        
        # just iterate from our border lol
        # add these to visited
        # in our overall loop if curr == o and not visited, replace with X

        # much simpler solution

        # approach iteratively with bfs

        queue = deque()
        for i in range(len(board)):
            queue.append((i, 0))
            queue.append((i, len(board[i])-1))
        for j in range(len(board[i])-2):
            queue.append((0, j+1))
            queue.append((len(board)-1, j+1))
        
        # perform bfs
        visited = set()
        while queue:
            qlen = len(queue)
            for k in range(qlen):
                i,j = queue.popleft()
                if (i,j) in visited:
                    continue
                
                # not visited yet
                # if out of bounds, continue
                if not (i in range(len(board)) and j in range(len(board[i]))):
                    continue
                
                # if not an O, continue
                if board[i][j] == "X":
                    continue
                
                # this is an unvisited, in bounds, X connected to our border
                visited.add((i,j))
                queue.append((i+1, j))
                queue.append((i-1, j))
                queue.append((i, j+1))
                queue.append((i, j-1))
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"

                        
                
