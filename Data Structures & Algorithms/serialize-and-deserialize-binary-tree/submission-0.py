# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # can't do iterative bfs because then need to populate every single null

    # dfs?
    # we might as well make a string of dfs


    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoding = self.traverse(root)
        print(encoding)
        return encoding
            
    def traverse(self, node: Optional[TreeNode]) -> None:
        if not node:
            return "N, "
            
        
        # node exists
        # add itself
        val = f"{node.val}, "
        val += self.traverse(node.left)
        val += self.traverse(node.right)
        return val

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return self.buildTree(data)

    def buildTree(self, data: str):
        arr = data.split(", ")
        print(arr)
        
        i = 0
        def builder():
            nonlocal i
            
            if i >= len(arr):
                return None
            
            val = arr[i]
            i+=1

            if val == 'N':
                return None
            
            curr = TreeNode(val)
            curr.left = builder()
            curr.right = builder()
            return curr
        return builder()  
        
        # node exists
        # build current
        
        
        

