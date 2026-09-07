class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create weighted edges between nodes?
        # explore the cost of travelling from one node to another
        # opposite direction is 1/cost
        # create both directions when initializing the graph
        
        # loop over all the equations and values
        # populate adjacency list to and from
        # and store the cost associated with (from,to) and (to,from)
        
        # go through queries, perform dfs to locate the value, keep track of 
        # the multiplication cost to get there
        # if we do not locate our target, return -1
        # explore our neighbors, add current to visited so we don't cycle
        # we need to maintain our current multiple
        # and if the current equals target, set global multiple to that multiple
        # and exit
        # at each call, check to see if that global multiple is set
        # if it is, exit because we've found a solution in another branch
        # source: (dest, cost)
        adjacency = defaultdict(list)

        for i in range(len(equations)):
            adjacency[equations[i][0]].append((equations[i][1], values[i]))
            adjacency[equations[i][1]].append((equations[i][0], 1/values[i]))
        # adjacency list populated with costs
        def dfs(curr, target, visited):
            if curr == target:
                return 1
            
            if curr in visited:
                return -1
            
            # we haven't visited this yet
            visited.add(curr)
            # explore neifhbors of curr
            exploration = -1
            for (neighbor, cost) in adjacency[curr]:
                exploration = max(exploration, cost * dfs(neighbor, target, visited))

            # if we never found target, the answer will be negative,
            # so the max will be -1
            # if we found target, the answer will be positive
            return exploration
        out = []
        for query in queries:
            source = query[0]
            dest = query[1]
            if source not in adjacency or dest not in adjacency:
                out.append(float(-1))
                continue
            # try to explore to locate our target value
            
            result = dfs(source, dest, set())
            out.append(result)
        
        return out


    
