# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we need to explore the deepest route to None
        # if none, return 0
        
        def dfs(curr):
            if not curr:
                return 0
            
            # curr isn't null, keep exploring
            return 1 + max(dfs(curr.left), dfs(curr.right))
        
        return dfs(root)