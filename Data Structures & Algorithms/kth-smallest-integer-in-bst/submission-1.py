# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        # k'th value explore in inorder traversal
        # need to do it recursively
        
        # let's maintain a global variable 
        tracker = k
        sol = None
        def dfs(curr):
            nonlocal sol
            nonlocal tracker
            if sol:
                return

            if not curr:
                return
            
            dfs(curr.left)
            tracker-=1
            if tracker == 0:
                sol = curr.val
                return
            dfs(curr.right) 

            # after we explore we need to check to see if we're the k'th
            
        dfs(root)
        return sol