# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # can't fix directions
        # need to just determine max distance from left and max distance
        # from right and add one
        globalmax = 0
        def dfs(curr):
            nonlocal globalmax
            if not curr:
                return -1
            
            # we are not null. Explore how long we can go on the left and right
            # and compute the max we can do.
            # we have to track a global max
            # only pass up single direction
            left = 1 + dfs(curr.left)
            right = 1 + dfs(curr.right)
            # pass up only either left or right
            # but globally track globalmax as left+right
            globalmax = max(globalmax, left+right)
            print(curr.val, left, right)
            return max(left, right)
        
        dfs(root)
        return globalmax
