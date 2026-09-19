class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return true if this graph is acyclic
        # we need to determine if we ever re-encounter a visited node with in a traversal
        # populate an adjacency list
        # at each step, we need to explore all neighbors
        # if this current node has been visited, return False
        # otherwise, add it to visited and explore

        adjacency = defaultdict(list)
        for pair in prerequisites:
            # 1 is a prerequisite for 0
            # make 1 point to 0
            adjacency[pair[1]].append(pair[0])
            if pair[0] not in adjacency:
                adjacency[pair[0]] = []
        

        
        
        # this computes if there is a cycle
        # visited needs to be local to the cycle
        visited = set()
        def dfs(curr, path):

            # cycle
            if curr in path:
                return True
            
            # already explored, no cycle from here
            if curr in visited:
                return False

            visited.add(curr)
            path.add(curr)

            # we haven't visited this yet
            # explore all neighbors
            for neighbor in adjacency[curr]:
                if dfs(neighbor, path):
                    return True
            path.remove(curr)
            return False
        
        # search for a cycle on all nodes if we haven't already explored
        # how do we avoid an overall re-exploration
        # global visited set?

        for node in adjacency:
            # only try this if it has a key in the hashmap
            if node not in visited:
                #print(node)
                hascycle = dfs(node, set())
                if hascycle:
                    return False
        
        return True
            
