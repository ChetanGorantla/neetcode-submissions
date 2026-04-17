class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency lists for each course
        # the adjacency list stores whichever courses this is a prerequisite for
        # (the adjacency list stores i,j,k... courses that can be built upon x)

        # once the adjacency list has been created, 

        # if you encounter a loop, return false

        # what does it mean to enter a loop?
        # say you start at node a, which is a prerequisite for b and c
        # then you look at b, which is a prerequisite for a and d
        # since the newest element already exists in the current path, return false
        # so we need to explore all paths that you can take given a starting node

        adjacency = {}
        # populate the adjacency list
        for courses in prerequisites:
            qualifier = courses[0]
            prereq = courses[1]
            if prereq in adjacency:
                adjacency[prereq].append(qualifier)
            else:
                adjacency[prereq] = [qualifier]
            
            if qualifier not in adjacency:
                adjacency[qualifier] = []
        print(adjacency)
        #adjacency list is populated
        #now we need to explore all of the nodes
        def explore(node, path):
            if node in path:
                print("Already explored " + str(node) + " from path " + str(path)  + ", FALSE")
                return False
            
            # the current node is not in the path.
            # add to path and explore all neighbors of this node.
            
            able_to_explore = False
            path.append(node)
            for neighbor in adjacency[node]:
                
                if not explore(neighbor, path):
                    return False
                
            path.pop()
            return True

        # explore all of the nodes inside of adjacency
        # or do we need to do that? can we just explore one of the nodes?
        # if we explore some arbitrary node, since the graph is connected,
        # it should be connected to all other nodes someway.
        # since the graph is connected, if there is a cycle somewhere in the graph, we will spot it
        # but actually, the graph is directed. Which means that even though the graph is 
        # connected, it is not strongly connected, it is weakly connected. Which means that
        # even though we can explore paths, it depends on where we start, which means we will just
        # have to explore all of the paths possible.

        for node in adjacency:
            if not explore(node, []):
                return False
        return True   
            
