# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # comare left child w curr and right child w curr
        # then ensure left dfs and right dfs are also true

        # we also need to pass down parent?
        # right child must be less than parent
        # there are additional bounds besides direct parent
        # we have a fixed bound that we must align by
        # this is based on the lowest and highest value we've seen along this path?
        # if we're comparing a right child, it needs to be within the lower and higher along this path
        # if we're comparing a left child, it needs to be within the lower and higher along this path

        def dfs(curr, l, h):
            if not curr:
                return True
            
            # what is a true path?
            # when curr has no children

            
            # if a child is null, that part is valid
            if not (not curr.left or (l < curr.left.val and curr.left.val < curr.val)):
                # valid
                return False
            if not (not curr.right or (curr.val < curr.right.val and curr.right.val < h)):
                # valid
                return False

            # pass down the compressed window
            # satisfied
            result = dfs(curr.left, l, curr.val) and dfs(curr.right, curr.val, h)
            #print(curr.val, result)
            return result
        
        # we are compressing our space
        return dfs(root, -sys.maxsize, sys.maxsize)

