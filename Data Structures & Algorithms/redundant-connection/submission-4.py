class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we need to locate the minimum cycle within the graph,
        # and based on all of the edges within this cycle, if we remove this edge,
        # will this graph stay connected? (will the two nodes still have an adjacency list of len > 0)
        # if so, if the indexOf this edge is greater than the current max, update it


        # so how do we find the minimum cycle in a graph?
        # 2 1 3 4 1
        # once we find a repeated part, we only consider the indexOf(last part) until the last part exclusive

        # create a possibility list of the adjacent edges within the cycle found 
        # (just loop over it 2 indices at a time)

        adjacency = {}
        
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if a in adjacency:
                adjacency[a].append(b)
            else:
                adjacency[a] = [b]
            
            if b in adjacency:
                adjacency[b].append(a)
            else:
                adjacency[b] = [a]
        
        # now that our adjacency list is initialized, we can make our dfs algorithm to search for cycles.
        cycle_edges = []

        def dfs(node, prev, path, path_set):
            if len(cycle_edges) > 0:
                return
            if node not in path_set:
                path_set.add(node)
                path.append(node)

                # visit this node and explore it's neighbors
                for neighbor in adjacency[node]:
                    if neighbor != prev:
                        dfs(neighbor, node, path, path_set)
                path.pop()
                path_set.remove(node)
            else:
                # cycle has been detected
                l = path.index(node)
                r = len(path)-1
                print(path[l:r+1])
                last_cycle_edge = sorted([path[l], path[r]])
                print("last: ", last_cycle_edge)
                # populate cycle edge list based on l and r
                while (l <= r-1):
                    cycle_edges.append(sorted([path[l], path[l+1]]))
                    l+=1
                if cycle_edges[0] != last_cycle_edge:
                    cycle_edges.append(last_cycle_edge)
                

        dfs(edges[0][0], -1, [], set([]))

        last_edge = []
        last_idx = -1
        print(cycle_edges)
        # go through the cycle edges and remove them
        for edge in cycle_edges:
            a = edge[0]
            b = edge[1]
            # we can technically remove any edge in this cycle.
            # just get the last index'd edge
            idx = edges.index(edge)
            if idx > last_idx:
                last_idx = idx
                last_edge = edge
        
        return last_edge
                



