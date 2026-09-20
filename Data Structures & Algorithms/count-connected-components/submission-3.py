class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we need to fully explore each connected component
        # populate an adjacency list
        # explore all nodes from here
        

        visited = set()
        adjacency = {}
        for i in range(n):
            adjacency[i] = []
        
        for u,v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        

        def dfs(curr, path):
            if curr in path:
                return
            
            # not visited yet
            path.add(curr)
            visited.add(curr)
            # explore neighbors
            for neighbor in adjacency[curr]:
                dfs(neighbor, path)
        
        c = 0
        for node in range(n):
            if node not in visited:
                c+=1
                dfs(node, set())
        
        return c
