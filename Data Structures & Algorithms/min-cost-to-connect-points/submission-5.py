class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # not necessarily min spanning tree
        # we need to keep global total cost in mind
        # maybe we should create an edge connecting every single node together?
        # that might take too long

        # i think it should actually be min spanning tree?
        # because summation of local optimals should equal global optimal?
        # construct MST from points?
        # for each point we need to make an edge with all other points and add that
        # to an adjacency list
        # what should our adjacency list look like? maybe we store each coordinate as the index
        # in the original points array
        # so maintain an addl indices hashmap
        # and in our adjacency list store ind_source: (dist, (x, y))

        # instead of making another indices hashmap, just tuplize the coords to be able to hash
        # then, we need to perform prim's algorithm on the adjacency list
        #initialize a priority queue (minheap)
        # start off at a certain node (candidate poll of minheap). 
        # if we've already visited this node, skip.
        # if we haven't visited this node, proceed.
        # mark this node as visited and add all unvisited neighbors into the priority queue
        # at the next iteration, we're going to pick a new candidate
        # while len(visited) < len(points) proceed

        
        # instead, maintain a list of the minimum distances from this coordinate to the MST
        n = len(points)
        mindist = [sys.maxsize] * n
        mindist[0] = 0
        mincost = 0
        visited = [False] * n

        for i in range(n):
            # find the mindist node in this iteration. that is our next candidate.
            curr = -1
            for j in range(n):
                if not visited[j] and (curr == -1 or mindist[j] < mindist[curr]):
                    curr = j
            
            
            # with that candidate, mark it as visited, and add its cost.
            visited[curr] = True
            mincost += mindist[curr]
            # now, update all other unvisited cells to possibly find new mindists for them
            # based on this new addition

            for j in range(n):
                if not visited[j]:
                    mindist[j] = min(mindist[j], abs(points[j][0]-points[curr][0]) + abs(points[j][1] - points[curr][1]))
            
            # updated all other distances
        return mincost

            
