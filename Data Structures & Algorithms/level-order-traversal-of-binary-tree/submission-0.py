# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q) #current breadth width
            level = [] 
            for i in range(qlen):#iterate through current breadth
                node = q.popleft() #remove node from queue and store temporarily
                if node: #if node is not null, get children
                    level.append(node.val) #add current node to output since its not null
                    q.append(node.left)
                    q.append(node.right) #append left and right children (even if null) to queue for next level
                
            if level:
                res.append(level) #if level is not entirely null, append it to output
        return res


        