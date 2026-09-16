# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we need to segment based on inorder
        # take the first value in preorder
        # find the index of that in inorder
        # segment both halves of inorder based on that
        # left child is l+1
        # right child is l+2
        # each recursive step is computing the current node and then attaching the children
        # based on future recursive calls
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i
        i = 0
        def construct(l, r):
            nonlocal i
            # get the index of this current element
            # if the index isn't in the window, return NULL
            if l > r:
                return None
            
            ind = indices[preorder[i]]
            
            # build the current node
            val = preorder[i]
            i+=1
            curr = TreeNode(val, construct(l, ind-1), construct(ind+1, r))
            return curr
        
        return construct(0, len(preorder)-1)