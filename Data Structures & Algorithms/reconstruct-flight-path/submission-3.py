class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # explore everything we can from here
        # and then append this to our path
        adjacency = defaultdict(list)
        tickets.sort()
        for u, v in tickets[::-1]:
            adjacency[u].append(v)

        path = []
        def dfs(curr):
            
            # explore all neighbors
            while adjacency[curr]:
                dest = adjacency[curr].pop()
                dfs(dest)
            path.append(curr)
        
        dfs("JFK")
        return path[::-1]
            
