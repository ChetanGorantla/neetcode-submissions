# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find lowest common ancestor of two nodes in the tree
        # we essentially need to go down from the root to determine the split path
        # the split path between p and q is the location of the lowest common ancestor
        if q.val < p.val:
            p, q = q,p
        curr = root
        while curr != p and curr != q:
            # check to see if we need to diverge from here
            if p.val < curr.val and curr.val < q.val:
                return curr
            
            if p.val < curr.val:
                curr = curr.left
            
            else:
                curr = curr.right
            
        # one is equivalent
        return curr