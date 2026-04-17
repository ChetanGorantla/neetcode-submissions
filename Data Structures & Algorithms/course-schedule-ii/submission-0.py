class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to build the graph first
        # iterate over all roots of connected components

        # the root of a connected component is a node that has an indegree of 0. 
        # note that there can only be one root of each connected component

        indegree = {}
        for edge in prerequisites:
            val = edge[0]
            enter = edge[1]
            if val not in indegree:
                indegree[val] = 1
            else:
                indegree[val] += 1
            
            if enter not in indegree:
                indegree[enter] = 0

        
        adjacency = {}
        for edge in prerequisites:
            val = edge[1]
            enter = edge[0]
            if val not in adjacency:
                adjacency[val] = [enter]
            else:
                adjacency[val].append(enter)
            
            if enter not in adjacency:
                adjacency[enter] = []
        
        # add any individual nodes
        for i in range(numCourses):
            if i not in adjacency:
                adjacency[i] = []
            if i not in indegree:
                indegree[i] = 0

        # our indegree list is populated
        # we want to explore all of the routes for each root, and simultaneously
        # check for any cycles, which if detected, should return an empty array to the system
        print("outdegree: ", adjacency)
        print("indegree: ", indegree)
        visited = {}
        for node in adjacency:
            visited[node] = False
        
        output = []
        queue = deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        print(queue)
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.popleft()
                output.append(node)

                for child in adjacency[node]:
                    indegree[child]-=1
                    if indegree[child] == 0:
                        queue.append(child)
        print(output)
        if len(output) != numCourses:
            return []
        return output
    