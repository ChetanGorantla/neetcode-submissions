import heapq
from collections import defaultdict
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # graph mincost path
        # construct a weighted adjacency list
        # at each index, we need to find the mincost path
        # from our current to our destination
        # use dijkstra's
        # maintain a minheap (totalcost, node)
        # when we explore a node, the cost to explore a neighbor
        # is totalcost+neighbor.cost
        # store edge cost as "cost to reach this node"

        adjacency = defaultdict(list)
        for i in range(len(original)):
            adjacency[original[i]].append((cost[i], changed[i]))
        
        # storing adjacency as curr -> (cost, dest)
        mintotalcost = 0
        # maybe we can memoize computations?
        memo = {}
        # values in the heap should be (cost, source, dest)
        for i in range(len(source)):
            heap = [(0, source[i])]
            visited = set()
            possible = False
            if (source[i], target[i]) in memo:
                mintotalcost += memo[(source[i], target[i])]
                continue

            while heap:
                edge = heapq.heappop(heap)
                currcost = edge[0]
                curr = edge[1]
                if curr in visited:
                    continue

                # first time visiting,
                # this is the mincost
                memo[(source[i], curr)] = currcost
                if curr == target[i]:
                    if not possible:
                        mintotalcost+=currcost
                    possible = True
                
                visited.add(curr)
                
                # we are not at our target yet
                # explore all unvisited neighbors
                for edge in adjacency[curr]:
                    dest = edge[1]
                    edgecost = edge[0]
                    heapq.heappush(heap, (currcost+edgecost, dest))
            if not possible:
                return -1
        
        return mintotalcost
                
