# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #global variable of the class

        #returns height, not diameter
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right) #current max height = current max vs left + right, returns EDGES
            return 1 + max(left, right) #current node is 1 + max of left and right is current height, returns HEIGHT
        dfs(root)
        return self.res