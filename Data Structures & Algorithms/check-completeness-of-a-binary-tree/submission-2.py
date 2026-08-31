# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # bfs?
        # first ensure that each level besides the last level is filled completely
        # first do dfs to figure out the max depth
        # then we do bfs
        # if this value is null and we are not at the last level
        # or this value is null and there are non-null elements remaining in the
        # queue
        # if we encounter a null value, that's our break condition
        
        # we actually just need to see if we encounter a null value
        # and we encounter a non-null and we've already encountered null
        # that's our canonical exit condition
        
        
        queue = deque()
        queue.append(root)
        while queue:
            poll = queue.popleft()
            if not poll:
                # make sure there are no more valid things left
                while queue:
                    if queue.popleft():
                        return False
                return True
            else:
                queue.append(poll.left)
                queue.append(poll.right)
        return True
                    