class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # maintain indegree and outdegree
        # we want to iterate over all nodes that have an indegree of 0
        # explore everything we can from there and prune indegree of neighbor -= 1
        # only add neighbors with indegree of 0 after pruning to simulate
        # the removal of this node

        indegree = {}
        adjacency = {}
        out = []
        for i in range(numCourses):
            indegree[i] = 0
            adjacency[i] = []
        for edge in prerequisites:
            u = edge[1]
            v = edge[0]

            adjacency[u].append(v)
            indegree[v]+=1
        
        # populated indegree and adjacency
        # maintain our queue
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        # we've populated our queue of all root nodes
        # now we want to perform traversal
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                # get curr
                curr = queue.popleft()
                out.append(curr)
                # explore all neighbors
                for neighbor in adjacency[curr]:
                    # prune
                    indegree[neighbor]-=1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        
        # out is now populated fully

        return out if len(out) == numCourses else []

