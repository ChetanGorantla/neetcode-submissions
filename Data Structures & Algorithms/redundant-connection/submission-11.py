class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # right now the graph is cyclic
        # remove an edge that would make it acyclic
        # determine the edges within the cycle
        # populate a list of edges that exist in the cycle
        # maintain the minimum cycle
        # do dfs
        
        # instead of building the cycle, we can prune the edge nodes from the graph
        # based on indegrees
        # after we're done pruning, we go through edges backwards to see if the edge exists
        
        # start from all nodes with an indegree of 1
        # do iterative bfs
        indegree = {}
        adjacency = {}
        edgeset = set()
        for u, v in edges:
            edgeset.add((min(u,v), max(u,v)))

        for u, v in edges:
            if u not in indegree:
                indegree[u] = 0
            if v not in indegree:
                indegree[v] = 0
            indegree[u] += 1
            indegree[v] += 1

            if u not in adjacency:
                adjacency[u] = []
            if v not in adjacency:
                adjacency[v] = []
            adjacency[u].append(v)
            adjacency[v].append(u)

        # indegree and adjacency populate
        queue = deque()
        for node in indegree:
            if indegree[node] == 1:
                queue.append(node)
                indegree[node]-=1
        
        # populated our queue with leaf nodes
        
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                curr = queue.popleft()
                print(curr)
                # explore the neighbors of this node
                for neighbor in adjacency[curr]:
                    # ensure we only explore neighbors which have an indegree of 0
                    
                    
                    # prune this connection
                    pruned = (min(curr, neighbor), max(curr, neighbor))
                    if pruned not in edgeset:
                        continue
                    indegree[neighbor]-=1
                    print("removing", pruned)
                    edgeset.remove(pruned)
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)
        
        # now we have our nodes pruned with the exception of nodes in cycles
        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            curr = (min(u, v), max(u,v))
            if curr in edgeset:
                return list(curr)
        
        return []
