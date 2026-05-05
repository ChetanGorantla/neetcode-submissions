# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        curr = root
        direction = -1
        # maintain current and parent
        # cycle whenever looking for the value
        while curr:
            # at a node, determine if we found or not
            if curr.val == key:
                # delete it

                
                
                # typical case split in 3: left present, right present, both present
                if curr.left and curr.right:
                    # cycle
                    # we can use the right node as the new basis, 
                    # but put the left subtree as it's leftmost descendant
                    basis = curr.right
                    left_descendant = basis
                    left_tree = curr.left
                    while left_descendant.left:
                        left_descendant = left_descendant.left
                    
                    left_descendant.left = left_tree

                    remaining = basis
                else:
                    # split case
                    remaining = curr.left if curr.left else curr.right
                    
                    
                
                if direction == 0:
                    parent.left = remaining
                elif direction == 1:
                    parent.right = remaining
                else:
                    return remaining
                
                return root


                

            else:
                # not found, determine where to go next
                if key < curr.val:
                    parent = curr
                    curr = curr.left
                    direction = 0
                else:
                    parent = curr
                    curr = curr.right
                    direction = 1

        # removal node not found
        return root

