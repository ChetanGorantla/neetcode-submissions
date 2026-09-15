# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do this in level order traversal
        # only do it on the last element (i == qlen-1)
        if not root:
            return []
        out = []
        queue = deque()
        queue.append(root)
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                curr = queue.popleft()
                
                # this means we can't append nulls because that would
                # cause inordering
                if i == qlen-1:
                    out.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return out