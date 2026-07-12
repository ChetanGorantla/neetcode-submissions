"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # just traverse the parents and keep track of visited? see the first crossover?
        visited = set()

        while p:
            visited.add(p)
            p = p.parent
        while q:
            if q in visited:
                return q
            visited.add(q)
            q = q.parent
        return None
    
    
        

        