# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #perform dfs on both?
        if not p and not q: #if BOTH are null, its same
            return True
        if p and q and p.val == q.val: #if both are not null and same value, its same
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #return if lefts are same and rights are same
        else: #if both are different, return false
            return False

            

