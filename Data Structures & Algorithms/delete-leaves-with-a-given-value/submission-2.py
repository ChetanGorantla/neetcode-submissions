# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # not a BST so we don't need to get a specific node
        # we just need to choose one of them. default to rightmost

        # we need to return the current node
        # 

        def reconstruct(node):

            # if this node is the target, we need to check to see if
            # we have children. if we don't return null
            # if we do, replace current with the right child
            # that should point to curr.left
            # return that
            # do a while loop?
            # while curr.val == target
            # that way we can go through all cases
            # instead of doing a while loop just call the recursive function on itself
            # if there is no right child, replace with left child instead

            # at the end, return curr


            # we are just deleting leaf nodes that match target


            if not node:
                return None
            
            
            """
            # otherwise, this may be a target but it's not a leaf node.
            if node.val == target and (node.left or node.right):
                # this is a target but not a leaf
                # try to reconstruct below this
                node.left = reconstruct(node.left)
                node.right = reconstruct(node.right)
                # after reconstruction, this is now a leaf target
                # return none
                if not node.left and not node.right:
                    return None
            else:
                """
            
            
            node.left = reconstruct(node.left)
            node.right = reconstruct(node.right)

            if node.val == target and not node.left and not node.right:
                return None

            
            return node

        return reconstruct(root)
