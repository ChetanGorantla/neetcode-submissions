class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # do we need to memoize min dist to edge given this edge
        # let's do it without trying to optimize first
        # we need to test each possible root
        # need to perform dfs on each root
        # we do need to store min dist to ending given this edge
        # that's how we store precomputed results
        # only do that when our origin is not the overall root
        # this only works when we're computing intermediary values
        if n == 1:
            return [0]
        # compute adjacency list
        adjacency = defaultdict(list)
        degree = [0] * n
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])
            degree[edge[0]]+=1
            degree[edge[1]]+=1
        
        # perform topological peel

        # strip away the leaves. because this is acyclic, we are guaranteed
        # to have leaves
        queue = deque()
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        level = 0
        remaining = n
        while remaining > 2:
            qlen = len(queue)
            remaining-=qlen
            for i in range(qlen):
                # strip away and add neighbors
                stripped = queue.popleft()
                for neighbor in adjacency[stripped]:
                    degree[neighbor]-=1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)
            


        