class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # once we find a virtual endpoint of the graph, we compare this with the max path length
        # just perform dijkstra's, include a running path sum which denotes priority of a node

        # how do we check to see if all nodes were visited?
        # track scratch
        # update scratch of each node visited
        # or keep a set of visited nodes
        # and at the end check to see if the set size is equal to n
        # if it is, return the maxpathlen
        # if not, return -1

        # create an adjacency list and an edge weight map

        adjacency = {}
        weights = {}

        for data in times:
            a = data[0]
            b = data[1]
            time = data[2]

            if a in adjacency:
                adjacency[a].append(b)
            else:
                adjacency[a] = [b]
            
            if b not in adjacency:
                adjacency[b] = []
            
            weights[(a, b)] = time

        weights[(0, k)] = 0
        # now that we've populated the adjacency list and edge weights, we can perform dijkstra's
        visited = set([])
        queue = []
        maxpath = 0

        # cost from starting node, dest node
        heapq.heappush(queue, (0,k))

        while queue:
            # poll a value
            curr = heapq.heappop(queue)
            
            # check to see if it hasn't been explored yet
            if curr[1] not in visited:
                weight = curr[0]
                a = curr[1]

                visited.add(a)
                maxpath = max(maxpath, weight)
                for dest in adjacency[a]:
                    if dest not in visited:
                        # update the path weight
                        edge = (weight + weights[(a, dest)], dest)
                        heapq.heappush(queue, edge)
                
            
        if len(visited) == n:
            return maxpath
        else:
            return -1

        