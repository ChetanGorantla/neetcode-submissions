class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        # for node in adjacency list, if not visited, explore it's connected graph
        # increment count

        # that way when we have reached an unvisited node on a new iteration that means 
        # we have found a new connected component of the graph
        if n == 1 and len(edges) == 0:
            return 1

        adjacency = {}
        for edge in edges:
            initial = edge[0]
            end = edge[1]
            if initial in adjacency:
                adjacency[initial].append(end)
            else:
                adjacency[initial] = [end]
            
            if end in adjacency:
                adjacency[end].append(initial)
            else:
                adjacency[end] = [initial]
        
        
        visited = {}
        for node in adjacency:
            visited[node] = False
        
        # now that we've populated the adjacency list, create our dfs algorithm
        def dfs(node, initial):
            if not visited[node]:
                visited[node] = True
                # explore neighbors
                density = 1
                for neighbor in adjacency[node]:
                    if neighbor != initial:
                        density += dfs(neighbor, node)
                return density
            else:
                return 0
        
        # need to count the number of nodes inside of this connected component also
        total_connected = 0
        count = 0
        for node in adjacency:
            if not visited[node]:
                count+=1
                total_connected += dfs(node, -1)

        return count + (n-total_connected)
