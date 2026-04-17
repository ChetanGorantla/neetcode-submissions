# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # keep a map of the listnode's we're at in a given linked list
        nodes = {}
        for i in range(len(lists)):
            # assign the listnode to it's respective index
            nodes[i] = lists[i]
        
        build = ListNode(-1, None)
        out = build

        # out of all the possible choices, pick the minimum
        # and create that node
        # and shift the pointer respectively
        
        
        while nodes:
            # for all values in the current search, get the min
            minimum = sys.maxsize
            located_idx = 0
            for i in range(len(lists)):
                
                if i in nodes and nodes[i].val < minimum:
                    minimum = nodes[i].val
                    located_idx = i
                    
            
            nodes[located_idx] = nodes[located_idx].next
            if not nodes[located_idx]:
                del nodes[located_idx]
            
            # located the smallest value to choose
            build.next = ListNode(minimum, None)
            build = build.next
        
        return out.next

            

