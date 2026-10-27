# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # use a maxheap to store k largest sums
        # when we need to return result return the -1'th element bc that's kth
        # iterative bfs to go level order easily
        # at each level compute the sum and add that to the maxheap




        levelsums = []
        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            level = 0
            for i in range(qlen):
                curr = queue.popleft()
                if not curr:
                    continue
                level+=curr.val
                queue.append(curr.left)
                queue.append(curr.right)
        
            if level == 0:
                continue
            heapq.heappush(levelsums, level)
            if len(levelsums) > k:
                heapq.heappop(levelsums)




        #print(levelsums)
        if len(levelsums) < k:
            return -1
        return levelsums[0]