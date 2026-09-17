"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # perform dfs to explore all of this node's neighbors
        # during that call, be populating a new node and populate neighbors with the dfs call

        # there are no cycles in the graph
        # this changes a lot

        # we have to create the clone BEFORE our next dfs call
        # so that it's reference is ready and available
        if not node:
            return None
            
        clones = {}
        def dfs(curr):
            if curr in clones:
                return clones[curr]
            
            # haven't explored this yet
            copy = Node(curr.val)
            clones[curr] = copy
            for nbr in curr.neighbors:
                # we need to create a copy
                copy.neighbors.append(dfs(nbr))
            return copy
        return dfs(node)