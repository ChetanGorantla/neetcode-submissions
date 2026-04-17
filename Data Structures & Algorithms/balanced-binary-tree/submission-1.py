# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #output in terms of [bool, val] [balanced, height]
        def dfs(root):
            if not root:
                return [True, 0] #base case is that its at the bottom node and its true
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])] #current node height
        return dfs(root)[0]

        
        