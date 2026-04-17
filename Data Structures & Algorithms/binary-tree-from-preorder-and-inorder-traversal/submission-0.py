# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder doesn't tell us anything about the nulls
        # we can use inorder to validate that

        # the first value of preorder is the root
        # maybe we can locate that in the inorder list
        # and work our way outwards in 2 pointer fashion?
        # use the property that we can partition based on pivots
        # for inorder traversal
        # so based on our pivot position we just need to figure out the 
        # ordering of stuff

        # look at the left partition
        # 
        # 1 | 2 3 | 4 5 6 7
        # preorder
        # 1 2 4 5 3 6 7
        # inorder
        # 4 2 5 1 6 3 7

        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            # get the root_val
            root_val = preorder[self.pre_idx]
            # increment pre_idx
            self.pre_idx+=1
            root = TreeNode(root_val)
            # get the index of the root_val in the inorder list
            middle_idx = indices[root_val]
            # partition and recursively call
            root.left = dfs(l, middle_idx-1)
            root.right = dfs(middle_idx+1, r)
            return root
            # return new constructed node
        return dfs(0, len(inorder)-1)