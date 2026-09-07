class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # check to see if we can reach target from this node
        # store a memoized result?
        # perform dfs

        adjacency = defaultdict(list)
        for prerequisite in prerequisites:
            adjacency[prerequisite[0]].append(prerequisite[1])
        
        # adjacency list has been built
        memo = {}
        def dfs(curr, target):
            if curr == target:
                return True
            
            if (curr, target) in memo:
                return memo[(curr, target)]
            
            # hasn't been explored yet
            possible = False
            for neighbor in adjacency[curr]:
                possible = possible or dfs(neighbor, target)
            memo[(curr, target)] = possible
            return possible
        
        out = []
        for query in queries:
            out.append(dfs(query[0], query[1]))
        
        return out

