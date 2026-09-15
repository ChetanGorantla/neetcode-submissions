# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check to see at any position, is subRoot achievable from curr
        # if not, check the children

        def sameTree(curr, sub):
            if not curr and not sub:
                return True
            if not curr or not sub:
                return False
            
            return curr.val == sub.val and sameTree(curr.left, sub.left) and sameTree(curr.right, sub.right)
        # we are just checking for equivalency
        def dfs(curr, sub):
            # we need to track exact equality
            # check to see if our current search is the same tree
            if not sub:
                return True
            if not curr:
                return False
            
            # we have a valid search space
            # check equality
            return sameTree(curr, sub) or dfs(curr.left, sub) or dfs(curr.right, sub)
        
        return dfs(root, subRoot)
        
        

                
            