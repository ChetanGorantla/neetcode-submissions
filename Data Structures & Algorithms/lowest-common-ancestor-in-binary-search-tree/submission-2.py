# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # define a function to find this node in the tree
        # go based on middle
        # say given p and q
        # we are at node m
        # if m is between p and q, this is the answer, because the paths diverge from here
        # if m is less than p and q, explore m.right
        # if m is greater than p and q, explore m.left
        # need a case for equality
        # if at least one is equal, then that equal node is the answer because we found it first

        # force p to be the smaller node
        if p.val > q.val:
            p, q = q, p

        m = root
        # loop to see while m is not null

        while m:            
            
            # shift case
            if p.val < m.val and q.val < m.val:
                m = m.left
            elif p.val > m.val and q.val > m.val:
                m = m.right
            else:
                return m
        
        return null
            

