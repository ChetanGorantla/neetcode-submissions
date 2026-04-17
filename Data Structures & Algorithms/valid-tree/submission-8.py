class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we need to check 2 things, that each node has between 0 and 2 children,
        # and that there are no cycles.

        # if these two conditions are true, then our tree is valid.
        if n == 1:
            if len(edges) == 0:
                return True
            else:
                return False

        # create an adjacency list
        adjacency = {}
        # store each node as the key and each outgoing node as the values
        visited = set([])
        # maybe don't store it as an adjacency list, but rather a connectivity list?
        # so [0,1] should store 1 for 0 and 0 for 1
        for edge in edges:
            curr = edge[0]
            nxt = edge[1]
            if curr in adjacency:
                adjacency[curr].append(nxt)
            else:
                adjacency[curr] = [nxt]
            
            if nxt in adjacency:
                adjacency[nxt].append(curr)
            else:
                adjacency[nxt] = [curr]

        

        
        print(adjacency)
        def dfs(node, parent):
            # this is a cycle
            if node in visited:
                print("Revisiting " + str(node) + " " + str(visited))
                return False
            
            
            # this has valid children. We can explore it now
            visited.add(node)
            valid = True
            for child in adjacency[node]:
                if parent != child:
                    print(str(node) + " visiting " + str(child))
                    valid = valid and dfs(child, node)
            
            return valid
        
        
        origin = edges[0][0]
        if origin not in visited:
            if not dfs(origin, -1):
                print("Exiting")
                return False
        print(adjacency)
        print(visited)
        return len(adjacency) == len(visited)
            
