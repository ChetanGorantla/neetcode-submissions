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

        adjacency = defaultdict(list)
        
        def distance(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        for source in points:
            for dest in points:
                if source != dest:
                    # create an edge between these
                    adjacency[(source[0], source[1])].append((distance(source, dest), (dest[0], dest[1])))

        # adjacency list is populated
        # now perform prims algorithm
        heap = [(0, (points[0][0], points[0][1]))]
        mincost = 0
        visited = set()
        while heap:
            curr_edge = heapq.heappop(heap)
            cost = curr_edge[0]
            curr = curr_edge[1]
            if curr in visited:
                continue
            mincost += cost
            visited.add(curr)
            # explore all unvisited neighbors
            for edge in adjacency[curr]:
                dist = edge[0]
                neighbor = edge[1]
                if neighbor not in visited:
                    heapq.heappush(heap, edge)
        return mincost
            
