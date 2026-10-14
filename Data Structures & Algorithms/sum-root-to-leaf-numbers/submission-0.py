# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # construct the prefix at each node
        # pass in the previous prefix in your dfs call
        # set current prefix to be prev*10 + curr.val
        # initial dfs call should be (root, 0)

        # if we are at a leaf node (both children are null) then add to a total sum

        totalsum = 0
        def dfs(curr, prev):
            nonlocal totalsum
            if not curr:
                return
            
            value = prev*10 + curr.val
            if not curr.left and not curr.right:
                totalsum+=value
                return
            
            # extend
            dfs(curr.left, value)
            dfs(curr.right, value)
        
        dfs(root, 0)
        return totalsum
            
