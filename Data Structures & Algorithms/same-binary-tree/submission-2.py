# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if equivalent in terms of exact structure
        # check to see if current is equivalent
        # then check to see if dfs(left) and dfs(right)
        # honestly I want to do this iteratively instead of recursively
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            stack1len = len(stack1)
            stack2len = len(stack2)
            if stack1len != stack2len:
                return False
            
            # we need to pop, compare, and append
            for i in range(stack1len):
                p1 = stack1.pop()
                p2 = stack2.pop()
                #print(p1, p2)
                
                if p1.val != p2.val:
                    return False
                
                # add children if they exist
                # if one child exists but the other doesnt, return false
                if (p1.left and not p2.left) or (not p1.left and p2.left):
                    return False
                if (p1.right and not p2.right) or (not p1.right and p2.right):
                    return False
                if p1.left and p2.left:
                    stack1.append(p1.left)
                    stack2.append(p2.left)
                if p1.right and p2.right:
                    stack1.append(p1.right)
                    stack2.append(p2.right)
        print(stack1)
        print(stack2)
        return True