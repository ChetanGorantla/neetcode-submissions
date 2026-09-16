# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # only continue with this path if its > 0
        # otherwise there's no point
        # extend the max path sum from the left vs right
        
        overallmax = -sys.maxsize
        def dfs(curr):
            nonlocal overallmax
            if not curr:
                return 0
            
            # curr exists.
            # we need to check to see the left path sum and right path sum
            leftpath = dfs(curr.left)
            rightpath = dfs(curr.right)
            # current path = max(0, curr.val + leftpath + rightpath)
            path = curr.val + leftpath + rightpath
            
            overallmax = max(path, overallmax)
            # if path is negative, pass up 0 but still consider 0 for the overallmax
            
            # you can only pass up the larger of leftpath + curr or rightpath + curr
            path = max(0, leftpath + curr.val, rightpath + curr.val)
            return path
        
        dfs(root)
        return overallmax