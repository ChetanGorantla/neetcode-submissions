# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # track the height of the left and right subtree
        # if they differ by more than 1 return false
        broken = False
        def dfs(curr):
            nonlocal broken
            if broken:
                return 0
            if not curr:
                return 0
            
            # 
            left_depth = dfs(curr.left)
            right_depth = dfs(curr.right)
            print(left_depth, right_depth)
            if abs(left_depth-right_depth) > 1:
                broken = True
            depth = 1 + max(left_depth, right_depth)
            return depth

        dfs(root)
        return not broken

