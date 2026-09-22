class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # minimum time it takes to span the whole tree
        # minimum spanning tree
        # ensure our visited set is the length of n

        adjacency = {}
        visited = set()
        for i in range(1, n+1):
            adjacency[i] = []
        for u,v,time in times:
            adjacency[u].append((time, v))
        
        # this is not MST
        # this is dfs
        # return the maximum time it takes to reach a single node,
        
        queue = []
        queue.append((0, k))
        maxtime = 0
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                curr = heapq.heappop(queue)
                node = curr[1]
                time = curr[0]

                if node in visited:
                    continue

                maxtime = max(maxtime, time)
                
                
                visited.add(node)
                # add the neighboring edges
                for edge in adjacency[node]:
                    heapq.heappush(queue, (time+edge[0], edge[1]))
        
        return maxtime if len(visited) == n else -1

