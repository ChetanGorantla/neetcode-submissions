# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if equivalent in terms of exact structure
        # check to see if current is equivalent
        # then check to see if dfs(left) and dfs(right)
        # honestly I want to do this iteratively instead of recursively
        # now let's try to solve it recursively

        # each recursive call must contain both nodes
        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return True
            
            if not curr1 or not curr2:
                return False
            
            # both are valid
            if curr1.val != curr2.val:
                return False
            
            # explore the children
            valid_children = dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right)
            return valid_children
        
        return dfs(p, q)
