# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # keep a global maximum and each time we do a dfs call, update the max(globalmax, localmax)
        globalmax = [root.val]

        def dfs(node):
            if node == None:
                return 0
            print("Exploring " + str(node.val))
            # add up the sum of the left and right children plus the current
            

            # we can either choose both subtrees, one of them, just this node,
            # or none
            

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # update global max
            globalmax[0] = max(globalmax[0], node.val + left + right)

            return node.val + max(left, right)
        
        dfs(root)
        return globalmax[0]