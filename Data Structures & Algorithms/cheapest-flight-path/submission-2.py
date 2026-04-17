class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # this is just prim's algorithm
        # and at each node you have to track which flight count this is
        # and if it's flight count is equal to k then once you're done processing it
        # don't add its neighbors into the queue

        # at each step, poll the shortest path
        # if it's flight count is equal to k, look to see if we're at the target and update min
        # if flight count is less than k, add all neighbors to the queue

        
        adjacency = {}
        prices = {}

        for flight in flights:
            source = flight[0]
            dest =  flight[1]
            cost = flight[2]
            if source in adjacency:
                adjacency[source].append(dest)
            else:
                adjacency[source] = [dest]
            
            if dest not in adjacency:
                adjacency[dest] = []
            
            prices[(source, dest)] = cost

        # we've initialized our adjacency list, we can start with prim's algorithm
        # within our minheap we must store (cost, node, flight_count)
        minheap = []
        mincost = sys.maxsize
        visited = set([])

        heapq.heappush(minheap, (0, src, 0))
        
        while minheap:
            curr = heapq.heappop(minheap)
            
            cost = curr[0]
            node = curr[1]
            flight_count = curr[2]
            print(curr)
            # if we already visited this node, continue
            #if node in visited:
            #    continue

            # we have not explored this node yet

            #visited.add(node)
            if node == dst:
                mincost = min(mincost, cost)
            else:
                if flight_count < k+1:
                    # if we can still travel further, explore all neighbors
                    for neighbor in adjacency[node]:
                        heapq.heappush(minheap, (cost + prices[(node, neighbor)], neighbor, flight_count+1))
                # otherwise don't do anything

            
        return -1 if mincost == sys.maxsize else mincost






