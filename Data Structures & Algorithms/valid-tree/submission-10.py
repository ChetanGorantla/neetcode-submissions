class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # can't think in terms of parents and children
        # we must ensure that all nodes are connected and acyclic
        # we can use topological sort to prune connections and explore all
        # parts of the graph
        # if at the end, our visited set isn't the same length as n, return false
        # because that means not all were connected.
        # compute indegree and outdegree
        adjacency = {}

        for i in range(n):
            adjacency[i] = []
        
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        
        # adjacency lists populated
        # now we call iterative bfs on any node
        # do we even need to do this? 
        # can we just maintain a visited list? 
        
        visited = set()
        stack = [0]

        # do this with iterative dfs
        # so we can track our parent at a given curr
        # to not re-explore that

        parents = set()
        visited.add(0)
        while stack:
            curr = stack.pop()
            
            # not visited yet
            # explore neighbors that arent my parent
            for neighbor in adjacency[curr]:
                # we are about to explore (curr, neighbor)
                if (neighbor, curr) in parents:
                    continue
                
                # we are about to explore a non-parent
                # check to see if neighbor isn't already visited
                if neighbor in visited:
                    return False
                
                # not in visited
                visited.add(neighbor)
                parents.add((curr, neighbor))
                stack.append(neighbor)
                
        return len(visited) == n
        

                
                