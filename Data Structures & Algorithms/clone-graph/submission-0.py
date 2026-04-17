"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if (not node):
            return None
        
        clones = {}
        def dfs(node):
            
            if (node not in clones):
                print("Visiting node ", node.val)
                copy = Node(node.val)
                clones[node] = copy
                for nbr in node.neighbors:
                    copy.neighbors.append(dfs(nbr))
                return copy
            else:
                return clones[node]
        root = dfs(node)
        return root