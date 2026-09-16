# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # bfs traversal
    # to encode

    # to decode we use a multiplier to see how many elements we want to
    # iterate over at a certain level, and we maintain a queue
    # when decoding, we set the first value as the root
    # pop until len of queue, look at 2 values at a time, those are the children
    # set curr.left and curr.right
    # append curr.left and curr.right into the queue
    # ensure we cast to an int when building the node
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque()
        queue.append(root)
        out = []
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                curr = queue.popleft()
                if not curr:
                    out.append("null")
                    continue
                
                # curr exists
                out.append(str(curr.val))
                # add its children to the queue
                queue.append(curr.left)
                queue.append(curr.right)
        #print("Finished serializing")
        #print(out)
        return " ".join(out)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # we have data in the form of "1 2 3"
        vals = data.split(" ")
        if vals[0] == "null":
            return None
        queue = deque()
        root = TreeNode(int(vals[0]))
        queue.append(root)
        i = 1
        while queue:
            qlen = len(queue)
            for j in range(qlen):
                curr = queue.popleft()
                # if curr is null, we want to just continue
                # because we can't do anything with this.
                if not curr:
                    continue
                    
                # for this value, we want to read 2 data values from vals
                # those are the children of curr.
                leftchild = int(vals[i]) if vals[i] != "null" else None
                rightchild = int(vals[i+1]) if vals[i+1] != "null" else None
                i+=2
                if leftchild:
                    curr.left = TreeNode(leftchild)
                    queue.append(curr.left)

                if rightchild:
                    curr.right = TreeNode(rightchild)
                    queue.append(curr.right)
        #print("Finished deserializing")
        return root

