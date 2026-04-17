class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create a graph
        # where each edge represents that a comes before b in the dictionary
        # if we find a new node to insert, insert it where it belongs and reestablish connections

        # at each step, we need to consider the current 2 iterating strings
        # curr and prev
        # loop until we find a letter greater in curr
        # curr's char must be greater than prev's char
        # create an adjacency list

        # in our backtracking algorithm
        # we need to explore for circuits and simultaneously append nodes to our result
        # keep track of visited nodes within a path
        # within our call if this node is visited then we've found a cycle so immediately return empty string
        # if not visited, we need to explore all it's children
        # then at the end mark it as unvisited for the backtracking part

        # loop this call over all unexplored nodes in our graph
        # so that we catch any disconnected components or standalone nodes


        adjacency = {}
        # initialize adjacency
        for char in words[0]:
            adjacency[char] = []


        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]

            for char in curr:
                if char not in adjacency:
                    adjacency[char] = []

            idx = 0
            while idx < len(prev) and idx < len(curr) and prev[idx] == curr[idx]:
                idx+=1
            # we have either looped out of one of the strings or located two mismatched chars

            # if we are still within the strings, we have found a valid ordering
            if not (idx == len(prev) or idx == len(curr)):
                # populate this directed edge
                a = prev[idx]
                b = curr[idx]
                adjacency[a].append(b)
            else:
                if len(curr) < len(prev):
                    return ""
        
        print(adjacency)

        


        # now that our adjacency list has been populated, we can make our dfs call
        visited = {}
        output = []

        def dfs(node):
            # if it's in visited, don't just return true, return whether or not a cycle was formed
            # from this node
            if node in visited:
                return visited[node]
            
            # this node hasn't been visited in this path yet. explore it's children
            
            visited[node] = True
            #print("Exploring node " + str(node))
            
            for dest in adjacency[node]:
                if dfs(dest):
                    return True
        
            visited[node] = False
            output.append(node)
            return False
        
        for node in adjacency:
            if dfs(node):
                return ""
        
        output.reverse()
        return "".join(output)
                    

        
        
        


            






        

        

