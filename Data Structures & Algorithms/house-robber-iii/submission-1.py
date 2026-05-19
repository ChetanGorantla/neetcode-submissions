# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at each step, we have choices:
        # skip current and take whichever children are valid
        # take current if both children invalid

        

        # we need to backtrack, i don't think we can do this in one pass
        # not a greedy algorithm since we need to explore multiple options in the scope of global context

        # within a dfs call, compute the result given children validity inputs, current node input
        # find the max of the choices and return that as the result
        # explore all choices within the call

        # what if instead of looking down, we look up
        # so the input is the parent rather than the children

        # if the parent is taken, we skip this child
        # if the parent is not taken, we take the child or skip the child
        # either way, one option is we skip the child
        
        # we need to memoize somehow
        # 2d dp
        money = {}
        
        def dfs(curr, parent_taken):
            # base case
            if not curr:
                return 0
            
            if (curr, parent_taken) in money:
                return money[(curr, parent_taken)]
            
            # valid node, look at parent condition
            taken = 0
            # if the parent is not taken, we take current
            if not parent_taken:
                taken = curr.val + dfs(curr.left, True) + dfs(curr.right, True)
            # either way we simulate a skip
            skipped = dfs(curr.left, False) + dfs(curr.right, False)

            path = max(skipped, taken)
            money[(curr, parent_taken)] = path
            return path
        
        return dfs(root, False)

            