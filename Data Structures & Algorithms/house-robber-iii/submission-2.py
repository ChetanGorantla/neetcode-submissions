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


        # we can actually optimize - we can skip 2d dp by doing 1d dp based on singular node state
        # but actually compute in advance instead of maintaining a second state
        money = {}

        def dfs(curr):
            if not curr:
                return 0

            if curr in money:
                return money[curr]
            
            # node not visited yet, compute

            # two options: 
            # take the current node and recurse on grandchildren
            # skip the current node and recurse on children

            take = curr.val
            if curr.left:
                take += dfs(curr.left.left) + dfs(curr.left.right)
            if curr.right:
                take += dfs(curr.right.left) + dfs(curr.right.right)
            
            # skip
            skip = dfs(curr.left) + dfs(curr.right)

            optimal = max(take, skip)
            money[curr] = optimal
            return optimal
        
        return dfs(root)
            
        
        

            