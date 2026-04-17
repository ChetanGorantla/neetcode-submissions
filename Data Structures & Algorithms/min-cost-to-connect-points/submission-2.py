class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algorithm
        # priority queue based on cost between two points
        # minheap
        # track visited

        
        if len(points) == 1:
            return 0

        # create an adjacency list and an edge weight map
        adjacency = {}
        weights = {}
        coords = {}
        for i in range(len(points)):
            a = points[i][0]
            b = points[i][1]
            coords[(a,b)] = i

        # store points in terms of just indices of the original points list

        # compute the distance between all points on the map
        for pair1 in points:
            for pair2 in points:
                if pair1 != pair2:
                    # compute the distance
                    x1 = pair1[0]
                    y1 = pair1[1]
                    x2 = pair2[0]
                    y2 = pair2[1]
                    dist = abs(x1-x2) + abs(y1-y2)
                    # create this edge
                    idx1 = coords[(x1, y1)]
                    idx2 = coords[(x2, y2)]

                    weights[(idx1, idx2)] = dist
                    
                    if idx1 in adjacency:
                        adjacency[idx1].append(idx2)
                    else:
                        adjacency[idx1] = [idx2]
                    
                    


        # our adjacency list and weights have been created
        print(adjacency)
        print(weights)

        # now we need to perform prim's algorithm
        minheap = []
        path = 0
        visited = set([])

        heapq.heappush(minheap, (0, 0))

        while minheap:
            # pop this value
            curr = heapq.heappop(minheap)
            weight = curr[0]
            coord = curr[1]
            if coord in visited:
                continue
            
            visited.add(coord)
            #print(f"Path node: {coord} has weight of {weight}")
            
            path += weight
            
            for dest in adjacency[coord]:
                if dest not in visited:
                    heapq.heappush(minheap, (weights[(coord, dest)], dest))
        
        return path






