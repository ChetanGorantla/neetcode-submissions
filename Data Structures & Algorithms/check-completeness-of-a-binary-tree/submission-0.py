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
        
        
        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        maxdepth = dfs(root)
        print(maxdepth)

        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            qlen = len(queue)
            depth+=1
            for i in range(qlen):
                # pop candidate
                poll = queue.popleft()
                if not poll:
                    # we aren't at the maxdepth. early break
                    if depth < maxdepth:
                        return False
                    # we are at the max depth. check to see if there are any
                    # non null values remaining
                    while queue:
                        if queue.popleft() != None:
                            return False
                    # no false conditions met. this is valid
                    return True
                else:
                    # this is a valid element.
                    # add its children
                    queue.append(poll.left)
                    queue.append(poll.right)
        return True
                    