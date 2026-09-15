# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # path from root to curr contains no value greater than curr
        # pass down max along path
        # compare curr with max
        # if curr >= max, add count
        # initial maxpath needs to be root.val
        count = 0
        def dfs(curr, maxpath):
            nonlocal count

            if not curr:
                return
            # this value exists. compare it with maxpath
            if curr.val >= maxpath:
                count+=1
            maxpath = max(curr.val, maxpath)
            dfs(curr.left, maxpath)
            dfs(curr.right, maxpath)
        
        dfs(root, root.val)
        return count
            
